#!/usr/bin/env python3
"""
모든 코딩 문제 시각화를 렌더링하는 통합 스크립트
4가지 문제의 Manim 애니메이션을 생성합니다.
"""

import subprocess
import os
import sys
from pathlib import Path


def render_scene(scene_file: str, scene_class: str, quality: str = "medium_quality"):
    """
    Manim 씬을 렌더링합니다.

    Args:
        scene_file: Python 파일명 (확장자 제외)
        scene_class: 렌더링할 Scene 클래스명
        quality: 렌더링 품질 (low_quality, medium_quality, high_quality)
    """
    cmd = [
        "manim",
        f"{scene_file}.py",
        scene_class,
        f"-{quality[0]}",  # l, m, h
    ]

    print(f"\n{'='*60}")
    print(f"렌더링: {scene_file} - {scene_class}")
    print(f"명령어: {' '.join(cmd)}")
    print(f"{'='*60}")

    try:
        result = subprocess.run(cmd, check=True, capture_output=False)
        print(f"✓ {scene_class} 렌더링 완료!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {scene_class} 렌더링 실패: {e}")
        return False


def main():
    """모든 시각화를 렌더링"""

    # 렌더링할 씬 목록
    scenes_to_render = [
        ("two_sum_visualization", "TwoSumVisualization", "Two Sum (배열/HashMap)"),
        ("tree_level_order_visualization", "BinaryTreeLevelOrderVisualization", "Binary Tree Level Order (BFS)"),
        ("dp_make_one_visualization", "DPMakeOneVisualization", "1로 만들기 (DP)"),
        ("sort_visualization", "SortVisualization", "수 정렬하기 (정렬)"),
    ]

    print("\n" + "="*60)
    print("AI-Powered 코딩 문제 시각화 렌더링")
    print("="*60)
    print(f"총 {len(scenes_to_render)}개의 씬을 렌더링합니다.\n")

    # 각 씬 렌더링
    results = []
    for file_name, class_name, description in scenes_to_render:
        print(f"\n[{len(results)+1}/{len(scenes_to_render)}] {description}")
        success = render_scene(file_name, class_name, quality="medium_quality")
        results.append((description, success))

    # 결과 요약
    print("\n" + "="*60)
    print("렌더링 결과 요약")
    print("="*60)

    success_count = 0
    for description, success in results:
        status = "✓ 성공" if success else "✗ 실패"
        print(f"{status}: {description}")
        if success:
            success_count += 1

    print(f"\n총 {success_count}/{len(results)} 완료")

    if success_count == len(results):
        print("\n🎉 모든 시각화 렌더링이 완료되었습니다!")
        print("\n생성된 비디오 파일:")
        print("  - media/videos/two_sum_visualization/medium_quality/TwoSumVisualization.mp4")
        print("  - media/videos/tree_level_order_visualization/medium_quality/BinaryTreeLevelOrderVisualization.mp4")
        print("  - media/videos/dp_make_one_visualization/medium_quality/DPMakeOneVisualization.mp4")
        print("  - media/videos/sort_visualization/medium_quality/SortVisualization.mp4")
        return 0
    else:
        print("\n⚠️  일부 시각화 렌더링에 실패했습니다.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
