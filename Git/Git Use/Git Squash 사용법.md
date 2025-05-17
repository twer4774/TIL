여러 commit을 하나로 합쳐 Git 이력을 정리하는 기능
- 코드 히스토리가 깔끔해지고 직관성이 높아져, 불필요한 commit들을 정리할 수 있다.

## 필요 이유
- 로컬 레포지토리에서 여러 commit 이후 리모트 레포지토리에 push하거나 pull request를 날리는 등 중요한 작업 전에 squash로 불필요한 commit들을 정리해준다.

## 사용방법
1. 브런치 생성 및 스위칭
2. 여러 commit 생성 & push & pull request
3. Squash할 commit 선정
	1. git log로 내역 확인
	2. Rebase 편집기 실행 
		1. git rebase -i HEAD~N # 최근 N개의 커밋
	3. 편집기에서 commit2의 pick -> squash로 변경 후 저장 (pick 기준은 하나 있어야함)
	4. commit 메시지 수정 후 저장
	5. git log로 내역 재확인
4. git push
	1. 이미 push나 pull request에 반영되어 있으므로 강제 옵션으로 해주어야 한다.
		1. git push origin feature/branchA --force

## 참고
- 다른 브런치들의 메시지도 묶어서 하나의 브런치로 변경 가능하다.
```
branchA 커밋들
branchB 커밋들
=> git switch -c branchC

branchC에서 rebase를 이용해 다른 커밋들을 squash해서 올려서 해결
```