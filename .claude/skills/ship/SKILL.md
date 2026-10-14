---
name: ship
description: 변경 사항을 git add . → commit → push 한 번에 올린다. 사용자가 /ship 을 입력했을 때만 실행.
disable-model-invocation: true
argument-hint: "[커밋 메시지(선택)]"
---

# /ship — add, commit, push

사용자가 넘긴 인자: `$ARGUMENTS`

다음 순서로 진행한다. 중간에 실패하면 멈추고 에러 메시지를 한국어로 짧게 설명한다.

1. `git status --porcelain` 으로 변경 사항을 확인한다. 아무것도 없으면 "올릴 변경 사항이 없어요."라고 말하고 끝낸다.
2. 민감한 파일 확인: `.env`, `*.pem`, `*key*.json` 등 비밀 정보로 보이는 파일이 추가 대상에 있으면 **커밋하지 말고** 사용자에게 알린 뒤 `.gitignore` 추가를 제안한다.
3. `git add .`
4. 커밋 메시지:
   - `$ARGUMENTS` 가 비어 있지 않으면 그대로 사용한다.
   - 비어 있으면 `git diff --cached --stat` 를 보고 한국어 한 줄로 요약해 만든다 (예: "Day 2 문제 풀이", "Day 3 개념 설명·문제 추가").
5. `git commit -m "<메시지>"`
6. `git push` (업스트림이 없으면 `git push -u origin <현재 브랜치>`).
7. 결과를 한두 줄로 보고한다: 커밋 메시지, 올라간 파일 수, push 성공 여부.
