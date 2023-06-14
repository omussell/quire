import secrets

english_conversion_table = """
CODE-0  B-70  P-80  NUM-90
A-1     C-71  Q-81  (.)-91
E-2     D-72  R-82  (:)-92
I-3     F-73  S-83  (')-93
N-4     G-74  U-84  ( )-94
O-5     H-75  V-85  (+)-95
T-6     J-76  W-86  (-)-96
        K-77  X-87  (=)-97
        L-78  Y-88  REQ-98
        M-79  Z-89  SPC-99
"""


english_code_book = """
000 ABORT        253 DECODE        505 MILITARY     758 STREET
019 ACCEPT       262 DELAY         514 MONEY        767 SUBWAY
028 ACCESS       271 DIFFICULT     523 MONTH        776 SUCCESS
037 ADDRESS      280 DOCUMENT      532 MORNING      785 SUPPLY
046 AFFIRMATIVE  299 ENCODE        541 MORSE        794 SUPPORT
055 AGENT        307 EVENING       550 NEGATIVE     802 TELEPHONE
064 AIRPLANE     316 EXECUTE       569 NIGHT        811 TODAY
073 AIRPORT      325 FACTORY       578 OBSERVATION  820 TOMORROW
082 ANSWER       334 FAILED        587 PASSPORT     839 TRAIN
091 AUTHORITY    343 FERRY         596 PERSON       848 TRANSFER
109 BETWEEN      352 FLIGHT        604 PHOTOGRAPH   857 TRANSMIT
118 BORDER       361 FREQUENCY     613 POSITIVE     866 TRAVEL
127 BUILDING     370 HARBOUR       622 POSSIBLE     875 TRUCK
136 CANCEL       389 HELICOPTER    631 POWER        884 UNABLE TO
145 CHANGE       398 HIGHWAY       640 PRIORITY     893 URGENT
154 CIVILIAN     406 IDENTITY      659 PROBLEM      901 VERIFY
163 COMPROMISE   415 IMMEDIATE     668 QUESTION     910 WEEK
172 COMPUTER     424 IMPOSSIBLE    677 RADIO        929 WITHIN
181 CONFIRM      433 INFORMATION   686 RECEIVE      938 YESTERDAY
190 CONTACT      442 INSTRUCTIONS  695 RENDEZVOUS   947 .........
208 COORDINATE   451 LOCATE        703 REPEAT       956 .........
217 COUNTRY      460 LOCATION      712 RESERVATION  965 .........
226 COVERT       479 MAIL          721 ROUTINE      974 .........
235 CURRENT      488 MEETING       730 SATELLITE    983 .........
244 DANGER       497 MESSAGE       749 SHIP         992 .........
"""


def random_pad():
    random_number_pad = ''.join(str(secrets.randbelow(10)) for i in range(250))
    chunks = [random_number_pad[i:i+25] for i in range(0, len(random_number_pad), 25)]
    
    for chunk in chunks:
        row = [chunk[i:i+5] for i in range(0, len(chunk), 5)]
        print(" ".join(row))
    print("-" * 30)

for _ in range(50):
    random_pad()
print(english_conversion_table)
print(english_code_book)
