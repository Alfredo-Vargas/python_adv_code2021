<!-- The description of the parsing for day16 is quite long and condition dependent so
I decided to make a summary and some diagrams to help elucidate the best solution -->

### Rules

1. The hexadecimal representation of this packet **might** encode a few extra $0$ bits at the end that should be ignored.
2. Every packet has a standard header: **first three bits** encode the packet **version** and the **next three bits** the **packet type ID**.
3. **Literal values** are packets with **type ID** $4$. The content of literal value can be represented by groups of five bits, one containing the prefix and the other the number value.

```mermaid
flowchart LR
  S[Type ID == 4] --> D5s[Extract group of 5 bits];
  D5s --> G1{is first bit 1?} -->|YES| C[read number, next 4 bits];
  G1{is first bit 1?} -->|NO| LG[read next number, next 4 bits\n complete with zeros if needed];
  C --> D5s;
  LG --> END;
```

4. **Operators** are packets with **type ID** $\neq 4$. An operator can contain one or more packets. The header of an operator is followed by the **length type ID**. If the length type ID is $15$ it represents the **total lenght in bits** of the sub-packets contained by this packet. If $1$, then it represents the **number of sub-packets immediately contained** by this packet.

```mermaid
flowchart LR
  S[Type ID != 4] --> LTID{Is length type 0?};
  LTID{Is length type 0?} --> |YES|GL[Get Length in bits of \n subpackets contained];
  LTID{Is length type 0?} --> |NO|GN[Get number of subpackets \n contained immediately after];
```

### Second Part

- The flow diagram when one needs to consider the operations is as follows:

```mermaid
flowchart
  START[binary\npacket];
  FINISHED{Has subpackets?};
  PARSE[Parse\n Version & ID];
  CHECK{Is ID = 4?}
  LITERAL[Process Literal];
  OPERATOR[Process Operator];
  RETURNL[Return Literal];
  GETLT{IS LENGTH TYPE 0?};
  NBS[Get Nbits in subpacket\n Encoded in next 15 bits];
  NS[Get N of Subpackets\nEach of 11 bits];
  GV0[A = Start Default Value];
  GV1[B = GET VALUE];
  CHANGED[IF B = -1 &&\n SUM => B = 0\n PROD => B = 1\n MAX => B = 0\n MIN => B = 999];
  OPERATE[RESULT = A OP B];
  RETURNR[Return RESULT];
  
  START --> FINISHED;
  FINISHED -->|NO| RETURN[Return -1];
  FINISHED -->|YES| PARSE;
  PARSE --> CHECK;
  CHECK -->|YES| LITERAL;
  LITERAL --> RETURNL;
  CHECK -->|NO| OPERATOR;
  OPERATOR --> GV0;
  GV0 --> GETLT;
  GETLT -->|YES| NBS;
  GETLT -->|NO| NS;
  NS --> GV1;
  NBS --> GV1;
  GV1 --> START;
  GV1 --> CHANGED;
  CHANGED --> OPERATE;
  OPERATE --> RETURNR;
```
