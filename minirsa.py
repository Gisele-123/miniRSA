from decimal import *
from tqdm import tqdm

N = Decimal(1615765684321463054078226051959887884233678317734892901740763321135213636796075462401950274602405095138589898087428337758445013281488966866073355710771864671726991918706558071231266976427184673800225254531695928541272546385146495736420261815693810544589811104967829354461491178200126099661909654163542661541699404839644035177445092988952614918424317082380174383819025585076206641993479326576180793544321194357018916215113009742654408597083724508169216182008449693917227497813165444372201517541788989925461711067825681947947471001390843774746442699739386923285801022685451221261010798837646928092277556198145662924691803032880040492762442561497760689933601781401617086600593482127465655390841361154025890679757514060456103104199255917164678161972735858939464790960448345988941481499050248673128656508055285037090026439683847266536283160142071643015434813473463469733112182328678706702116054036618277506997666534567846763938692335069955755244438415377933440029498378955355877502743215305768814857864433151287)
e = Decimal(3)
c = Decimal(1220012318588871886132524757898884422174534558055593713309088304910273991073554732659977133980685370899257850121970812405700793710546674062154237544840177616746805668666317481140872605653768484867292138139949076102907399831998827567645230986345455915692863094364797526497302082734955903755050638155202890599808154521995312832362835648711819155169679435239286935784452613518014043549023137530689967601174246864606495200453313556091158637122956278811935858649498244722557014003601909465057421728834883411992999408157828996722087360414577252630186866387785481057649036414986099181831292644783916873710123009473008639825720434282893177856511819939659625989092206115515005188455003918918879483234969164887705505900695379846159901322053253156096586139847768297521166448931631916220211254417971683366167719596219422776768895460908015773369743067718890024592505393221967098308653507944367482969331133726958321767736855857529350486000867434567743580745186277999637935034821461543527421831665171525793988229518569050)

def int_to_ascii(m):
    # Decode to ascii (from https://crypto.stackexchange.com/a/80346)
    m_hex = hex(int(m))[2:-1]  # Number to hex
    m_ascii = "".join(
        chr(int(m_hex[i : i + 2], 16)) for i in range(0, len(m_hex), 2)
    )  # Hex to Ascii
    return m_ascii


# Find padding
getcontext().prec = 280  # Increase precision
padding = 0
for k in tqdm(range(0, 10_000)):
    m = pow(k * N + c, 1 / e)

    m_ascii = int_to_ascii(m)

    if "pico" in m_ascii:
        padding = k
        break

print("Padding: %s" % padding)

# Increase precision further to get entire flag
getcontext().prec = 700

m = pow(padding * N + c, 1 / e)
m_ascii = int_to_ascii(m)
print("Flag: %s" % m_ascii.strip())