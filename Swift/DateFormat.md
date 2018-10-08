# Swift DateFormat

| 포맷               | 설명                                                         | 예시                                                         |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| “y”                | 년도,   최소 1 글자 표시                                     | 1   AD →        “1”  <br /> 42   AD →     “42”   <br />2014   AD → “2014” |
| “yy”               | 년도,   2 글자 표시, 앞자리 공백 ‘0’ 으로 채움               | 1   AD → “01”   <br />42 AD → “42”   <br />2014   AD → “14”  |
| “yyy”              | 년도,   최소 3 글자 표시, 앞자리 공백 ‘0’ 으로 채움          | 1   AD →  “001”   <br />42   AD →  “042”   <br />2014   AD → “2014” |
| “yyyy”             | 년도,   최소 4 글자 표시, 앞자리 공백 ‘0’ 으로 채움          | 1   AD → “0001”   <br />42   AD → “0042”   <br />2014   AD → “2014” |
| “M”                | 월,   최소 1 글자 표시                                       | July → “7”   <br />December → “12”                           |
| “MM”               | 월,   최소 2 글자 표시, 앞자리 공백 ‘0’ 으로 채움            | July → “07”   <br />December → “12”                          |
| “MMM”              | 월,   3 단어 약자 표시                                       | July → “Jul”  <br /> December → “Dec”                        |
| “MMMM”             | 월,   이름                                                   | July → “July”   <br />December → “December”                  |
| “MMMMM”            | 월,   최소 1 글자 약자 표시(January, June, July 같은 경우 ‘J’ 로 동일하게 표현) | July → “J”  <br /> December → “D”                            |
| “d”                | 일,   최소 1 글자                                            | 4 → “4”   <br />25 → “25”                                    |
| “dd”               | 일,   2 글자 표시, 앞자리 공백 ‘0’ 으로 채움                 | 4 → “04”   <br />25 → “25”                                   |
| “E”, “EE”,   ”EEE” | 월,   3 단어 약자 표시                                       | Wednesday → “Wed”   <br />Thursday → “Thu”                   |
| “EEEE”             | 일,   이름                                                   | Wednesday → “Wednesday”   Thursday → “Thursday”              |
| “EEEEE”            | 일,   최소 1 글자 약자 표시(Tuesday, Thursday 같은 경우 동일하게 ’T’ 로 표현) | Wednesday → “W”   <br />Thursday → “T”                       |
| “EEEEEE”           | 일,   2 글자 약자 표시                                       | Wednesday → “We”   <br />Thursday → “Th”                     |
| “a”                | 오전,   오후                                                 | 5   PM → “PM”   <br />7   AM → “AM”                          |
| “h”                | 1-12   시간 표현, 최소 1 글자 표시                           | 5   PM → “5”   <br />7   AM → “7”                            |
| “hh”               | 1-12   시간 표현, 최소 2 글자 표시, 앞자리 공백 ‘0’ 으로 채움 | 5   PM → “05”   <br />7   AM → “07”                          |
| “H”                | 0-23   시간 표현, 최소 1 글자 표시                           | 5   PM → “17”   <br />7   AM → “7”                           |
| “HH”               | 0-23   시간 표현, 최소 2 글자 표시, 앞자리 공백 ‘0’ 으로 채움 | 5   PM → “17”   <br />7   AM → “07”                          |
| “m”                | 분,   최소 1 글자 표시                                       | 40 →   “40”   <br />1 → “1”                                  |
| “mm”               | 분,   최소 2 글자 표시, 앞자리 공백 ‘0’ 으로 채움            | 40 →   “40”   <br />1 → “01”                                 |
| “s”                | 초,   최소 1 글자 표시                                       | 40 →   “40”   <br />1 → “1”                                  |
| “ss”               | 초,   최소 2 글자 표시, 앞자리 공백 ‘0’ 으로 채움            | 40 →   “40”   <br />1 → “01”                                 |
| “S”                | 1   / 10 초 표시                                             | 123   ms → “1”   <br />7   ms → “0”                          |
| “SS”               | 1   / 100 초 표시                                            | 123   ms → “12”   <br />7   ms → “00”                        |
| “SSS”              | 1   / 1000 초 표시                                           | 123   ms → “123”   <br />7   ms → “007”                      |

 