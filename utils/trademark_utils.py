import re
import unicodedata
from datetime import date

import numpy as np
import pandas as pd

_DATE_PATTERN = re.compile(r'\((\d{4})\.(\d{1,2})\.(\d{1,2})\)')
_CLASS_PATTERN = re.compile(r'第(\d+)類')


def parse_filing_date(text: str) -> date | None:
    """出願日文字列から datetime.date を返す。パース失敗時は None。

    入力例: '平成２９年２月２０日（２０１７．２．２０）'
    処理:   全角→半角正規化 → カッコ内の YYYY.M.D を正規表現で抽出
    """
    if not isinstance(text, str):
        return None
    normalized = unicodedata.normalize('NFKC', text)
    m = _DATE_PATTERN.search(normalized)
    if not m:
        return None
    return date(int(m.group(1)), int(m.group(2)), int(m.group(3)))


def extract_classes(text: str) -> list[int]:
    """指定商品・役務文字列から区分番号（整数）のリストを返す。

    入力例: '第３０類  アイスクリーム...,第３５類  ...'
    処理:   全角→半角正規化 → 第N類 を正規表現で全抽出
    """
    if not isinstance(text, str):
        return []
    normalized = unicodedata.normalize('NFKC', text)
    return [int(n) for n in _CLASS_PATTERN.findall(normalized)]


_MAX_ENTROPY = float(np.log2(45))  # 全45区分均等分布のときの最大エントロピー


def calc_entropy(counts: pd.Series) -> dict:
    """区分別出願件数からShannon entropy（底2）を計算する。

    Args:
        counts: インデックス=区分番号、値=出願件数 の Series

    Returns:
        {
            'entropy':            Shannon entropy (bits),
            'entropy_normalized': entropy / log2(45)  → [0, 1],
            'n_classes_used':     出願ゼロでない区分の数,
            'total_applications': 総出願件数,
        }
    """
    counts = counts.reindex(range(1, 46), fill_value=0)
    total = int(counts.sum())
    if total == 0:
        return {
            'entropy': 0.0,
            'entropy_normalized': 0.0,
            'n_classes_used': 0,
            'total_applications': 0,
        }
    p = counts[counts > 0] / total
    entropy = float(-(p * np.log2(p)).sum())
    return {
        'entropy': round(entropy, 4),
        'entropy_normalized': round(entropy / _MAX_ENTROPY, 4),
        'n_classes_used': int((counts > 0).sum()),
        'total_applications': total,
    }
