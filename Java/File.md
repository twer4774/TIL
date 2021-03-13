# File

- File의 생성자와 경로와 관련된 메소드

| 생성자/메소드                                                | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| File(String fileName)                                        | 주어진 fileName을 이름으로 갖는 파일을 위한 File 인스턴스 생성. |
| File(String pathName, String fileName)<br />File(File pathName, String fileName) | 파일의 경로와 이름을 따로 분리해서 지정할 수 있도록 한 생성자.<br />두번째 메소드는 경로를 문자열이 아닌 File인스턴스인 경우를 위해 제공 |
| File(URI uri)                                                | 지정된 uri로 파일 생성                                       |
| String getName()                                             |                                                              |
| String getPath()                                             |                                                              |
| String getAbsoultePath()<br />File getAbsolutePath()         |                                                              |
| Stirng getParent()<br />File getParentFile()                 |                                                              |
| String getCanonicalPath()<br />File getCanonicalFile()       | 파일의 정규 경로를 Stirng으로 반환<br />파일의 정규 경로를 File로 반환 |

- 경로와 관련된 File의 멤버변수

| 멤버변수                      | 설명                                                  |
| ----------------------------- | ----------------------------------------------------- |
| static String pathSeparator   | OS에서 사용하는 path 구분자. 윈도우 "," / 유닉스  "." |
| static char apthSeparatorChar | 위와 동일                                             |
| static String separator       | OS에서 사용하는 이름 구분자. 윈도우 "\\" / 유닉스 "/" |
| static char separatorChar     | 위와 동일                                             |