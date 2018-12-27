# :-1/Users/jowon-ik/Desktop/\***/master/Pods/Pods/Target Support Files/Pods-\***/Pods-.debug.xcconfig: unable to open file (in target "" in project "") (in target '')

- git에서 프로젝트를 클론하면 발생하는 에러

  1. Target에서 cofiguration file을 none으로 설정
  2. .xcworkspace를 닫는다.
  3. Podfile.lock과 pods 폴더, .xcworkspace를 삭제한다.
  4. Pod install, pod update로 pods를 다시 설치한다.
  5. 프로젝트를 다시 연다. .xcworkspace로!
