import re
from collections import Counter

#frequency analysis
def analyze_frequencies(text):
    # count only letters
    letters_only = re.sub('[^A-Z]', '', text.upper())
    total_letters = len(letters_only)
    
    #unigrams
    letter_counts = Counter(letters_only)
    print("\n--- LETTER FREQUENCY (UNIGRAMS) ---")
    for letter, count in letter_counts.most_common(10):
        percent = (count / total_letters) * 100
        print(f"{letter}: {count} ({percent:.2f}%)")
        
    #bigrams
    bigrams = [letters_only[i:i+2] for i in range(len(letters_only)-1)]
    print("\n--- TOP 5 BIGRAMS ---")
    for bg, count in Counter(bigrams).most_common(5):
        print(f"{bg}: {count}")

    #trigrams
    trigrams = [letters_only[i:i+3] for i in range(len(letters_only)-2)]
    print("\n--- TOP 5 TRIGRAMS ---")
    for tg, count in Counter(trigrams).most_common(5):
        print(f"{tg}: {count}")

    return letter_counts

#mapping init
def create_initial_mapping():
    #set all text to _ as unknown
    return {chr(i): '_' for i in range(65, 91)}

def decrypt_display(text, mapping):
    result = ""
    for char in text:
        if char.isalpha():
            c_upper = char.upper()
            if mapping[c_upper] != '_':
                #lowercase letter for Plaintext
                result += mapping[c_upper]
            else:
                # uppercase letter for Ciphertext 
                result += c_upper
        else:
            # non-alphabetic characters remain unchanged
            result += char
    return result

def edit_mapping(text, mapping):
    print("\n" + "="*50)
    print("Syntax: [Cipher text] [Plain text]")
    print("'quit' to exit and print final mapping")
    print("="*50)
    
    while True:
        print("\n[CURRENTLY DECRYPTED]:\n")
        print(decrypt_display(text, mapping))
        print("\n" + "-"*50)
        
        cmd = input("Map (ex: G E) > ").strip().upper()
        
        if cmd == "QUIT":
            break
            
        parts = cmd.split()
        if len(parts) == 2 and parts[0].isalpha() and parts[1].isalpha():
            c, p = parts[0], parts[1]
            mapping[c] = p.lower()
        else:
            print("[!] Syntax error. Please enter the correct format (e.g., G E).")

# --------------------------------
# MAIN PROGRAM
# --------------------------------
ciphertext = """
Ghv Hliib Kzggvi svirvs, uirggvm yb Yirgrsh lfghzi Q.P. Izuormt, rs zmv zd ghv nzsg kzkfoli lmw rmdofvmgrlo dlmglsb sltls zd nzwvim orgvilgfiv. Sklmmrmt svevm yzzps, ghv svirvs dzoozus ghv ordv zd l bzfmt yzb, Hliib Kzggvi, uhz wrsxzevis zm hrs 11gh yrighwlb ghlg hv rs l urcliw. Hv rs rmergvw gz lggvmw Hztuligs Sxhzzo zd Urgxhxildg lmw Urcliwib, uhviv hv ovlims lyzfg hrs nltrxlo hvirgltv, wvevozks xozsv dirvmwshrks, lmw xzmdizmgs ghv wlip dzixvs ghlg ghivlgvm ghv urcliwrmt uziow.

Ghv xvmgilo kozg ivezoevs lizfmw Hliib's zmtzrmt ylggov urgh Oziw Ezowvnzig, l wlip urcliw rmgvmg zm xzmjfvirmt yzgh ghv nltrxlo lmw mzm-nltrxlo uziows. Ls Hliib tizus zowvi, hv ovlims nziv lyzfg hrs zum nbsgvirzfs klsg, hrs xzmmvxgrzm gz Ezowvnzig, lmw ghv kizkhvxb ghlg grvs ghvri dlgvs gztvghvi. Ghizfthzfg ghv svirvs, ghvnvs zd dirvmwshrk, ozblogb, yilevib, lmw ghv kzuvi zd ozev liv vakozivw, urgh l irxh uziow droovw urgh nltrxlo xivlgfivs, skvoos, lmw wvvk nbghzoztb.

Ghv yzzps, sgligrmt urgh Hliib Kzggvi lmw ghv Khrozszkhvi's Sgzmv (1997) lmw xzmxofwrmt urgh *Hliib Kzggvi lmw ghv Wvlghob Hloozus (2007), hlev szow zevi 500 nroorzm xzkrvs uziowurwv, yvvm gilmsolgvw rmgz nziv ghlm 80 olmtfltvs, lmw lwlkgvw rmgz l sfxxvssdfo dron svirvs. Ghv svirvs rs pmzum mzg zmob dzi rgs vmxhlmgrmt uziow-yfrowrmt yfg losz dzi lwwivssrmt wlipvi, xznkova ghvnvs sfxh ls nziglorgb, kivqfwrxv, lmw ghv lyfsv zd kzuvi. Ghv Hliib Kzggvi svirvs hls ovdg lm rmwvoryov nlip zm kzkfoli xfogfiv, dzsgvirmt l tozylo dlm ylsv, rmskrirmt xzfmgovss skrm-zdds, lmw xvnvmgrmt rgs kolxv ls l orgvilib khvmznvmzm.



Ervgmln Mlgrzmlo Fmrevisrgb, Hz Xhr Nrmh Xrgb (EMF-HXN) rs zmv zd ghv nzsg kivsgrtrzfs lmw xznkivhvmsrev hrthvi vwfxlgrzm rmsgrgfgrzms rm Ervgmln, pmzum dzi rgs vjxvoovmxv rm ivsvlixh, rmmzelgrzm, lmw vwfxlgrzm. Dzfmwvw rm 1995 yb ghv Ervgmlnvsv tzevimnvmg, EMF-HXN uls vsglyorshvw ls l pvb xvmgvi dzi gilrmrmt, ivsvlixh, lmw gvxhmzoztb gilmsdvi urgh ghv nrssrzm zd xzmgiryfgrmt gz ghv xzfmgib’s szxrz-vxzmznrx wvevozknvmg. Ls l doltshrk fmrevisrgb, rg hls kolbvw l krezglo izov rm kizwfxrmt hrthob sproovw kizdvssrzmlos, sxrvmgrsgs, lmw ovlwvis lxizss nfogrkov drvows.

EMF-HXN zkvilgvs fmwvi l wrsgrmxgrev sgifxgfiv ls l nfogr-wrsxrkormlib lmw nfogr-xlnkfs sbsgvn, xznkirsrmt svevilo nvnyvi fmrevisrgrvs lmw ivsvlixh rmsgrgfgvs. Ghvsv rmxofwv sznv zd ghv nzsg uvoo-vsglyorshvw rmsgrgfgrzms rm ghv ivtrzm, sfxh ls ghv Fmrevisrgb zd Sxrvmxv, Fmrevisrgb zd Gvxhmzoztb, Fmrevisrgb zd Szxrlo Sxrvmxvs lmw Hfnlmrgrvs, Rmgvimlgrzmlo Fmrevisrgb, Fmrevisrgb zd Vxzmznrxs lmw Olu, lmw zghvis. Vlxh zd ghvsv nvnyvi rmsgrgfgrzms zkvilgvs svnr-rmwvkvmwvmgob yfg xzoolyzilgvs fmwvi ghv fnyivool zd EMF-HXN, nlprmt rg l fmrafv hrthvi vwfxlgrzm nzwvo rm Ervgmln ghlg kiznzgvs rmgviwrsxrkormlib ovlimrmt lmw ivsvlixh.

Ozxlgvw rm Hz Xhr Nrmh Xrgb, ghv xzfmgib's vxzmznrx lmw xfogfilo hfy, EMF-HXN yvmvdrgs dizn xozsv grvs urgh rmwfsgirvs, yfsrmvssvs, lmw tzevimnvmg ltvmxrvs. Ghrs kizjrnrgb dzsgvis xzoolyzilgrzm rm ivsvlixh, rmgvimshrks, lmw qzy kolxvnvmg, vmsfirmt ghlg rgs tilwflgvs liv uvoo-kivklivw gz nvvg ghv wvnlmws zd lm vezoermt uzipdzixv. Ghv fmrevisrgb rs xznnrggvw gz kizwfxrmt tilwflgvs uhz liv mzg zmob lxlwvnrxloob kizdrxrvmg yfg losz vafrkkvw urgh kilxgrxlo sproos lmw l tozylo zfgozzp.

EMF-HXN rs ivmzumvw dzi rgs sgizmt vnkhlsrs zm sxrvmgrdrx ivsvlixh lmw gvxhmzoztrxlo rmmzelgrzm. Rg hzfsvs mfnvizfs ivsvlixh xvmgvis, rmsgrgfgvs, lmw olys ghlg dzxfs zm elirzfs livls zd sxrvmxv, vmtrmvvirmt, szxrlo sxrvmxvs, vxzmznrxs, lmw nziv. Ghv fmrevisrgb's ivsvlixh ltvmwl rs lortmvw urgh mlgrzmlo kirzirgrvs, dzxfsrmt zm livls sfxh ls rmdzinlgrzm gvxhmzoztb, yrzgvxhmzoztb, ivmvulyov vmvitb, lmw vmerizmnvmglo sfsglrmlyrorgb. EMF-HXN losz lxgrevob vmtltvs rm rmgvimlgrzmlo xzzkvilgrzm, kligmvirmt urgh ovlwrmt fmrevisrgrvs lmw ivsvlixh rmsgrgfgrzms uziowurwv gz vmhlmxv rgs lxlwvnrx kiztilns, dzsgvi qzrmg ivsvlixh kizqvxgs, lmw kiznzgv sgfwvmg lmw dlxfogb vjxhlmtvs.

Ghv fmrevisrgb rs losz wvvkob rmezoevw rm lwwivssrmt tozylo xhloovmtvs ghizfth rgs ivsvlixh lmw vwfxlgrzmlo kiztilns. EMF-HXN kolxvs l sgizmt vnkhlsrs zm sfsglrmlyov wvevozknvmg, vmerizmnvmglo xzmsvielgrzm, lmw gvxhmzoztrxlo rmmzelgrzm, lortmrmt rgs tzlos urgh ghv Fmrgvw Mlgrzms’ Sfsglrmlyov Wvevozknvmg Tzlos (SWTs). Ghv rmsgrgfgrzm vmxzfiltvs rgs dlxfogb lmw sgfwvmgs gz kfisfv ivsvlixh ghlg hls l nvlmrmtdfo rnklxg zm yzgh ghv ozxlo lmw tozylo xznnfmrgb.

Rm gvins zd sgfwvmg ordv, EMF-HXN zddvis l eryilmg lmw wbmlnrx vmerizmnvmg. Urgh l sgfwvmg yzwb zd zevi 60,000 lmw l dlxfogb zd hrthob aflordrvw kizdvsszis lmw ivsvlixhvis, ghv fmrevisrgb kizerwvs l irxh lxlwvnrx lmw szxrlo vjkvirvmxv. Ghv xlnkfsvs liv vafrkkvw urgh nzwvim dlxrorgrvs, rmxofwrmt oryilirvs, olyzilgzirvs, skzigs xznkovjvs, lmw wzinrgzirvs, xivlgrmt l sfkkzigrev ovlimrmt vmerizmnvmg. Sgfwvmgs losz hlev lxxvss gz l elirvgb zd vjgilxfiirxfoli lxgrergrvs, xofys, lmw zitlmrclgrzms, loozurmt ghvn gz vmtltv rm xfogfilo, szxrlo, lmw kizdvssrzmlo wvevozknvmg lozmtsrwv ghvri sgfwrvs.

Rm xzmxofsrzm, Ervgmln Mlgrzmlo Fmrevisrgb - Hz Xhr Nrmh Xrgb sglmws ls l ovlwrmt vwfxlgrzmlo rmsgrgfgrzm rm Ervgmln, xzmgiryfgrmt srtmrdrxlmgob gz ghv xzfmgib’s rmgvoovxgflo, sxrvmgrdrx, lmw vxzmznrx kiztivss. Rgs xznnrgnvmg gz lxlwvnrx vjxvoovmxv, ivsvlixh rmmzelgrzm, lmw szxrvglo rnklxg hls kzsrgrzmvw rg ls l xifxrlo kolbvi rm shlkrmt ghv dfgfiv zd Ervgmln lmw ghv yizlwvi ivtrzm. Ls rg xzmgrmfvs gz vezoev lmw vjklmw, EMF-HXN ivnlrms wvwrxlgvw gz dzsgvirmt ghv mvjg tvmvilgrzm zd ovlwvis lmw rmmzelgzis uhz uroo wirev sfsglrmlyov tizugh lmw tozylo kiztivss.
"""


letter_counts = analyze_frequencies(ciphertext)

mapping = create_initial_mapping()

edit_mapping(ciphertext, mapping)

print("\n===== FINAL MAPPING =====\n")
for k, v in sorted(mapping.items()):
    if v != '_':
        print(f"{k} -> {v}")