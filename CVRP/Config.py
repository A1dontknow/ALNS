import os


class Config:
    """
    Cac tham so se duoc mo ta nhu sau:

        * Nhung tham so nen giu co dinh:
        - D: Deterministic level cho Shaw Destroy. Khong co khac biet nhieu neu thay doi
        - DESTROY_RATIO: Muc pha huy nghiem trong destroy operator (tru MassiveDestroy).
        Muc Destroy nen de la 10%

        * Nhung tham so co the tinh chinh:
        - ITERATION: So vong lap thuc hien thuat toan. Khi cho chay du lau, thuat toan se
        co the tim duoc nhung nghiem tot hon, nhung khong co nghia la cang lau cang tot.
        Chay thuat toan song song voi so lan lap nao do co the la mot y tuong tot
        - SEGMENT: So phan doan cua thuat toan. Phan doan la cac doan chia Iteration.
        Tham so nay se quyet dinh so lan update trong so Destroy/Repair va so lan dung 
        Local Search
        - PHI_1: Diem thuong cho operator neu tim duoc nghiem tot nhat
        - PHI_2: Diem thuong cho operator neu tim duoc nghiem tot hon nghiem hien tai
        - PHI_3: Diem thuong neu nghiem tim duoc khong co su cai tien nao
        - N: Reaction factor - He so phan ung cua Adaptive Mechanism
        - V: Normalization factor - He so chuan hoa cua Adaptive Mechanism
        - DEVIATION: Chap nhan nghiem (ke ca nghiem xau hon) neu khong te hon mot nguong
        so voi nghiem tot nhat
        - BIG_DEVIATION: Chap nhan nghiem (ke ca nghiem xau hon) neu khong te hon mot nguong
        so voi nghiem tot nhat sau khi trai qua rat nhieu lan lap ma khong co su cai tien ve
        nghiem
        
        Reference: Ropke, S., & Pisinger, D. (2006) - An Adaptive Large Neighborhood Search 
        Heuristic for the Pickup and Delivery Problem with Time Windows. Transportation Science,
	40(4), 455–472. doi:10.1287/trsc.1050.0135

    """
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    D = 5
    ITERATION = 30000
    DESTROY_RATIO = 0.1
    SEGMENT = 300
    PHI_1 = 10
    PHI_2 = 6
    PHI_3 = 1
    # reaction factor
    N = 1
    # normalization factor
    V = 1
    # flat deviation
    DEVIATION = 30
    # broaden flat deviation
    BIG_DEVIATION = 100
