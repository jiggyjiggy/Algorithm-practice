'''

그래프를 탐색하기 위한 대표적인 알고리즘 두가지 DFS/BFS
stack & queue 사전지식으로 필요
stack & queue는 데이터 삽입, 삭제의 함수로 구성
+) overflow, underflow도 고려해야함

(1) stack
 FILO
 기본 list // append(), pop()

(2) queue
 FIFO
 from collections import deque // append(), popleft()
 deque = stack, queue의 장점을 모두 채택한 것 // list보다 데이터 입출력이 효율적임 // queue library 보다 간단
 deque object를 list 자료형으로 바꾸고 싶다면 list() 사용하면됌

(3) recursive function
 점화식으로 표현된다면 recursive function으로 구현하면 iterative적 구현보다 간결해짐
 종료조건 필수

 +) 컴퓨터 내부 구조와 메모리, 자료구조의 관계(코드수준이 아닌 논리회로?수준의)
 1. 코드레벨의 재귀함수를 쓰면
 2. 컴퓨터 내부에서의 실제 수행은 stack 자료구조를 이용한다
 3. 재귀함수의 논리적 구성을 보면 가장 마지막에 호출한 함수가 먼저 수행을 마쳐야 그 앞의 호출된 함수가 종료될 수 있기 때문이다

 4. 컴퓨터의 구조 측면: 연속해서 호출되어있는 함수들( <-뒤의 함수가 연산을 마무리해야 종료될 수 있는)은 메인메모리의 stack영역에 저장
 5. 이러한 측면에서 나온말이 재귀함수는 스택 자료구조와 동일하다는 소리

 6. 어쨌건 기억해야할 부분은
 7. 재귀함수의 내부적 동작원리는 스택 자료구조와 동일하다
'''