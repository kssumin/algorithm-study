
# Rule
1. **주차 별 문제 배정**
    - 매주 토요일에 5개의 문제가 배정된다.
2. **문제 해결 기한**
    - 문제는 매주 금요일 19시까지 해결해야 한다.
3. **벌금 규정**
    - 풀지 못한 문제당 5000원의 벌금이 있다.
4. **대면 회의 일정**
    - 매주 금요일 19시에 대면 회의를 진행한다.
5. **미해결 문제와 벌금**
    - 회의 전까지 완료하지 못한 문제는 풀지 못한 문제로 간주되며, 해당 문제에 대한 벌금이 부과된다.
6. **문제 풀이**
	-  문제를 해결할 수 없는 경우, 인터넷에 나와 있는 다른 사람의 문제 풀이를 참고하고 분석하여 올릴 시 해결한 것으로 간주한다.
7. **역할**
	- 문제 선정 : 박민규
	- Github 관리 : 김수민
	- 문서 관리 : 강바다
	- 총무 : 이지호
	- 리마인더 : 김종민


# 스터디 진행 방식

|용어|설명|
|:-:|:-:|
|upstream|kssumin/algorithm-study|
|origin|fork한 본인 레포지토리|


1. upstream 레포지토리를 fork한다.
  ![image](https://github.com/kssumin/algorithm-study/assets/71962076/0febd04c-1b52-4b76-b563-6d6b9243afe0)


	
3. fork한 저장소를 자신의 컴퓨터로 clone하고 폴더로 이동한다.
    - clone 명령은 github.com에 존재하는 저장소(remote 저장소)를 자신의 노트북(local 저장소)으로 복사하는 과정이다.
      `git clone https://github.com/{본인 아이디}/{저장소 아이디}.git`
    ![image](https://github.com/kssumin/algorithm-study/assets/71962076/776a2476-e871-4631-89ae-a72ecbcc4257)
    → 주소 확인은 이렇게 확인할 수 있습니다.
    

    
4. origin/main에서 매주 브랜치를 생성한다.

	주의할 점
	- **브랜치는 매주 생성해야 한다!**
	- **브랜치는 꼭 main에서 생성해야한다!**

 `git checkout -b {해당 주차}-{본인 이름}`
   
 ![image](https://github.com/kssumin/algorithm-study/assets/71962076/e6030597-c113-4acc-97e6-30302ee993b5)

6. 문제 별 파일 생성 후 풀이를 작성한다.
  ![image](https://github.com/kssumin/algorithm-study/assets/71962076/bf752fc1-0fa6-4a8a-a451-77882d69d107)

	- `backjoon_1000.js` 파일 생성 후 코드 작성

8. 풀이 파일을 add & commit 한다.
	- 기능 구현을 완료한 후 로컬 저장소에 변경된 부분을 반영하기 위해 add, commit 명령어를 사용한다.
		- `git add .` → 변경된 모든 파일 add
		- `git add {파일명}` → 특정 파일만 add
		- `git commit -m "[김수민] 백준 - 9733"`
		- `git commit -m "[김수민] 다익스트라 알고리즘"`
	- **add**

		<img width="871" alt="image" src="https://user-images.githubusercontent.com/88534959/221366418-08186092-0f9d-4d7b-b1b0-a9ab6cefd94a.png"><img width="935" alt="image" src="https://user-images.githubusercontent.com/88534959/221366469-bc4f8e45-ac8c-4662-a82d-589283ffa692.png">
	
	- **commit**, commit 명은 `[이름] 백준 - 알고리즘 번호`로 통일한다.
		![image](https://github.com/kssumin/algorithm-study/assets/71962076/67f9a9e0-9146-46ca-9d3b-e4dd26792eb7)

   
9. Github(원격 저장소)에 올린다.
    - 로컬에서 commit 명령을 실행하는 것은 로컬 저장소에 반영될 뿐, 원격 github.com의 저장소에는 반영되지 않는다.
	    - `git push origin 브랜치이름`
  ![image](https://github.com/kssumin/algorithm-study/assets/71962076/feccc1cc-3d2b-45d0-b066-3e032652a953)

10. Github 서비스에서 PR(pull request)를 보냅니다.
    - PR는 github에서 제공하는 기능으로 코드리뷰를 요청할 때 사용합니다.
    -  Create pull request 버튼을 클릭해 PR 내용을 작성한 후, Create pull request를 눌러 제출합니다.
  ![image](https://github.com/kssumin/algorithm-study/assets/71962076/b4516418-e6ff-42cc-8ed2-42b9305ed122)

	- Title : [x주차] {자신 이름} 문제풀이 제출합니다.
	- Description : 해당 주차의 문제 공지 이슈 번호 & 공유하고 싶은 정보
	- Assignees에 본인 추가하기. (`assign yourself` 클릭)
