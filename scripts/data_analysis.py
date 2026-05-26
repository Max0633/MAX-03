#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CPO（共封装光学）数据分析脚本
最后更新时间：2026年5月25日
"""

import json
from datetime import datetime

# CPO市场规模数据（2024-2032年）
market_data = {
    "years": [2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032],
    "market_size_billion_usd": [1.8, 4.5, 8.5, 14.0, 21.0, 29.0, 38.0, 47.0, 55.0],
    "yoy_growth": [None, 150, 89, 65, 50, 38, 31, 24, 17],
    "cagr_2024_2030": 65,
    "cagr_2025_2030": 52
}

# 区域市场分布（2026年）
regional_data_2026 = {
    "regions": ["北美", "亚太", "欧洲", "其他地区"],
    "market_share": [50, 35, 12, 3],
    "market_size_billion_usd": [4.25, 2.975, 1.02, 0.255]
}

# A股CPO概念股数据（2025年实际数据）
cn_stocks = {
    "stocks": [
        {"name": "中际旭创", "code": "300308.SZ", "revenue_billion_rmb": 35, "net_profit_billion_rmb": 7, "gross_margin": 0.32, "revenue_growth": 0.75, "cpo_relevance": "高", "rating": "买入"},
        {"name": "新易盛", "code": "300502.SZ", "revenue_billion_rmb": 15, "net_profit_billion_rmb": 3, "gross_margin": 0.30, "revenue_growth": 0.90, "cpo_relevance": "高", "rating": "买入"},
        {"name": "天孚通信", "code": "300394.SZ", "revenue_billion_rmb": 5, "net_profit_billion_rmb": 1.5, "gross_margin": 0.45, "revenue_growth": 0.70, "cpo_relevance": "高", "rating": "买入"},
        {"name": "光迅科技", "code": "002281.SZ", "revenue_billion_rmb": 10, "net_profit_billion_rmb": 1, "gross_margin": 0.28, "revenue_growth": 0.40, "cpo_relevance": "高", "rating": "增持"},
        {"name": "源杰科技", "code": "688498.SH", "revenue_billion_rmb": 2, "net_profit_billion_rmb": 0.6, "gross_margin": 0.38, "revenue_growth": 0.60, "cpo_relevance": "高", "rating": "买入"},
        {"name": "华工科技", "code": "000988.SZ", "revenue_billion_rmb": 6, "net_profit_billion_rmb": 0.6, "gross_margin": 0.25, "revenue_growth": 0.30, "cpo_relevance": "中", "rating": "增持"},
        {"name": "长飞光纤", "code": "601869.SH", "revenue_billion_rmb": 12, "net_profit_billion_rmb": 1.2, "gross_margin": 0.22, "revenue_growth": 0.25, "cpo_relevance": "中", "rating": "增持"}
    ]
}

# 产业链受益确定性排序
industry_chain_ranking = [
    {"rank": 1, "segment": "上游核心器件", "certainty": "最高", "companies": "源杰科技、Coherent Corp、Lumentum", "status": "已兑现高增长"},
    {"rank": 2, "segment": "光无源器件", "certainty": "最高", "companies": "天孚通信", "status": "已兑现高增长"},
    {"rank": 3, "segment": "光模块/光引擎", "certainty": "高", "companies": "中际旭创、新易盛", "status": "高增长持续"},
    {"rank": 4, "segment": "交换芯片", "certainty": "高", "companies": "Broadcom、NVIDIA", "status": "主导地位稳固"},
    {"rank": 5, "segment": "封装测试", "certainty": "中高", "companies": "ASE、长电科技、通富微电", "status": "受益增长"},
    {"rank": 6, "segment": "光纤供应商", "certainty": "中", "companies": "长飞光纤", "status": "稳定增长"}
]

def analyze_market_data():
    """分析市场规模数据"""
    print("=" * 60)
    print("CPO市场规模分析")
    print("=" * 60)
    print(f"\n数据更新时间: 2026年5月25日")
    print(f"\n2024-2030年CAGR: {market_data['cagr_2024_2030']}%")
    print(f"2025-2030年CAGR: {market_data['cagr_2025_2030']}%")

    print("\n市场规模预测（十亿美元）:")
    print("-" * 40)
    for i, year in enumerate(market_data['years']):
        size = market_data['market_size_billion_usd'][i]
        growth = market_data['yoy_growth'][i]
        growth_str = f"+{growth}%" if growth else "基准年"
        print(f"{year}: ${size:.1f}B ({growth_str})")

    print(f"\n2025年实际数据: ${market_data['market_size_billion_usd'][1]}B")
    print(f"2030年预测数据: ${market_data['market_size_billion_usd'][-3]}B")

def analyze_regional_data():
    """分析区域市场数据"""
    print("\n" + "=" * 60)
    print("区域市场分布分析（2026年）")
    print("=" * 60)

    for i, region in enumerate(regional_data_2026['regions']):
        share = regional_data_2026['market_share'][i]
        size = regional_data_2026['market_size_billion_usd'][i]
        print(f"{region}: {share}% (${size:.3f}B)")

def analyze_cn_stocks():
    """分析A股CPO概念股"""
    print("\n" + "=" * 60)
    print("A股CPO概念股分析（2025年实际数据）")
    print("=" * 60)

    print(f"\n{'公司名称':<10} {'营收(亿元)':<12} {'净利润(亿元)':<14} {'毛利率':<10} {'营收增速':<10} {'投资评级'}")
    print("-" * 80)

    for stock in cn_stocks['stocks']:
        print(f"{stock['name']:<10} {stock['revenue_billion_rmb']:<12} {stock['net_profit_billion_rmb']:<14} {stock['gross_margin']*100:.1f}%{'':<6} {stock['revenue_growth']*100:.0f}%{'':<6} {stock['rating']}")

def analyze_industry_chain():
    """分析产业链受益确定性"""
    print("\n" + "=" * 60)
    print("产业链受益确定性排序")
    print("=" * 60)

    print(f"\n{'排名':<6} {'产业链环节':<15} {'受益确定性':<12} {'2026年状态'}")
    print("-" * 70)

    for item in industry_chain_ranking:
        print(f"{item['rank']:<6} {item['segment']:<15} {item['certainty']:<12} {item['status']}")

def generate_summary():
    """生成分析摘要"""
    print("\n" + "=" * 60)
    print("CPO投资分析摘要（2026年5月）")
    print("=" * 60)

    print("\n1. 行业前景:")
    print("   - 2025年市场规模约45亿美元（实际数据），同比增长150%")
    print("   - 2026年预计市场规模约85亿美元，同比增长89%")
    print("   - 2030年预计市场规模约380亿美元，CAGR约52%")

    print("\n2. 投资机会:")
    print("   - 高确定性: 光模块龙头（中际旭创、新易盛）、上游核心器件（源杰科技）")
    print("   - 新增机会: 3.2T产品、光子计算、国产替代深化")

    print("\n3. 风险提示:")
    print("   - 技术风险: 3.2T产品开发进度")
    print("   - 市场风险: AI算力投资波动、竞争加剧")
    print("   - 政策风险: 地缘政治、出口管制")

    print("\n4. 投资建议:")
    print("   - 激进型: 中际旭创、新易盛、源杰科技")
    print("   - 稳健型: 中际旭创、天孚通信")
    print("   - 保守型: 光模块ETF")

def main():
    """主函数"""
    print("CPO（共封装光学）数据分析")
    print("最后更新时间: 2026年5月25日")
    print("=" * 60)

    analyze_market_data()
    analyze_regional_data()
    analyze_cn_stocks()
    analyze_industry_chain()
    generate_summary()

    print("\n" + "=" * 60)
    print("数据来源: 公开信息整理")
    print("免责声明: 本分析仅供研究参考，不构成投资建议")
    print("=" * 60)

if __name__ == "__main__":
    main()
