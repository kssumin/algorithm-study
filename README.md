# algorithm_study_version2

## Rule
- 스터디 결과로 나오는 산출물은 깃허브에 `매주 토요일 00시`까지 올립니다.
    - 자료구조/알고리즘 이론 공부 : 해당 주차의 공부 내역을 md 파일로 업로드합니다.
      - 해당 주차의 알고리즘 개념을 공부한 후, 정리한 내용을 `x주차/본인폴더`에  .md파일로 올립니다.
    - 코딩 테스트 문제 풀이
      - 문제를 못 풀겠는 경우, 인터넷에 나와있는 다른 사람의 문제풀이를 보고 분석해서 올립니다.
      - 문제 풀이 파일에 코드 뿐만 아니라 자신의 접근 방법을 적어놓고, 간단한 회고나 느낀점을 적습니다.
- PR에 대한 코드리뷰를 작성합니다.`일요일 00시까지`
- 스터디 진행 일정 : 매주 일요일 오전 9시 30분
  - 해당 스터디에서 이론 공부 내용을 발표합니다.
  - 이론에 대해 토론하던 중 해결하지 못한 질문이 있으면 Issue로 등록하여 다음주 일요일(00시)까지 issue에 댓글을 답니다.


## 스터디 진행 방법
1. fork한 저장소를 자신의 컴퓨터로 clone하고 폴더로 이동합니다.
    - clone 명령은 github.com에 존재하는 저장소(remote 저장소)를 자신의 노트북(local 저장소)으로 복사하는 과정입니다.

    `git clone https://github.com/{본인 아이디}/{저장소 아이디}.git`

2. 자신의 브랜치를 생성하고 이동합니다.

    `git checkout -b {본인 아이디}`

3. 문제를 풀고 add, commit 합니다.
   - 문제풀이 commmit 명은 `[이름] 백준 - 알고리즘 번호`로 통일합니다.
   - 이론 commit 명은 `[이름] 알고리즘 주제`로 통일합니다.
   - 기능 구현을 완료한 후 로컬 저장소에 변경된 부분을 반영하기 위해 add, commit 명령어를 사용합니다.
   
   `git add .`

   `git commit -m "[김수민] 백준 - 9733"`
   `git commit -m "[김수민] 다익스트라 알고리즘"`
     <img width="871" alt="image" src="https://user-images.githubusercontent.com/88534959/221366418-08186092-0f9d-4d7b-b1b0-a9ab6cefd94a.png">
     <img width="935" alt="image" src="https://user-images.githubusercontent.com/88534959/221366469-bc4f8e45-ac8c-4662-a82d-589283ffa692.png">
     <img width="1185" alt="image" src="https://user-images.githubusercontent.com/88534959/221366478-5ea6f5c4-6e73-412b-bdaa-5bc77cd8cb81.png">

4. 깃허브(원격 저장소)에 올립니다.
    - 로컬에서 commit 명령을 실행하는 것은 로컬 저장소에 반영될 뿐, 원격 github.com의 저장소에는 반영되지 않습니다.
   
   `git push origin 브랜치이름`
   <img width="988" alt="image" src="https://user-images.githubusercontent.com/88534959/221366490-d2647bf9-3fa7-4cd1-b9d9-fa836d87c945.png">


5. github 서비스에서 pull request를 보냅니다.
    - pull request는 github에서 제공하는 기능으로 코드리뷰를 요청할 때 사용합니다.

   `{자신의 브랜치}에서 {main 브랜치}로 pull request를 보냅니다.`
   <img width="864" alt="image" src="https://user-images.githubusercontent.com/88534959/221366758-384b131a-c6ed-4a72-9d08-c1457177da99.png">


6. Create pull request 버튼을 클릭해 PR 내용을 작성한 후, Create pull request를 눌러 제출합니다.
    - title : [x주차] {자신 이름} 문제풀이 제출합니다.
    - decription : 알게된 내용, 다른 사람들이 주의깊게 보면 좋을 부분을 적습니다.

7. 다른 사람의 코드를 리뷰해줍니다.
