import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

TOTAL_TIME = 1800   # 30 minutes

questions = [
    # (keep your SAME 80 questions list here)
# ===== BASIC =====
{"q":"Who developed Python?","o":["Dennis Ritchie","Guido van Rossum","James Gosling","Ken Thompson"],"a":"Guido van Rossum"},
{"q":"Python is which type language?","o":["Compiled","Interpreted","Assembly","Machine"],"a":"Interpreted"},
{"q":"Python file extension?","o":[".pt",".py",".p",".px"],"a":".py"},
{"q":"Keyword to define function?","o":["func","def","function","define"],"a":"def"},
{"q":"Symbol for comment?","o":["//","#","--","/*"],"a":"#"},
{"q":"Which is mutable?","o":["tuple","string","list","int"],"a":"list"},
{"q":"Which is immutable?","o":["list","set","dict","tuple"],"a":"tuple"},
{"q":"Input function?","o":["scan()","input()","get()","read()"],"a":"input()"},
{"q":"Output function?","o":["echo()","display()","print()","show()"],"a":"print()"},
{"q":"Keyword for loop?","o":["repeat","for","loop","iterate"],"a":"for"},

# ===== OPERATORS =====
{"q":"Exponent operator?","o":["^","**","//","%"],"a":"**"},
{"q":"Floor division operator?","o":["/","//","%","**"],"a":"//"},
{"q":"Modulus gives?","o":["Quotient","Remainder","Power","Sum"],"a":"Remainder"},
{"q":"Comparison operator?","o":["=","==","!=","Both a and b"],"a":"Both a and b"},
{"q":"Logical AND?","o":["&","and","&&","AND"],"a":"and"},
{"q":"Logical OR?","o":["|","or","||","OR"],"a":"or"},
{"q":"Not equal operator?","o":["<>","!=","~=","="],"a":"!="},
{"q":"Assignment operator?","o":["==","=","===","!="],"a":"="},
{"q":"Greater equal?","o":[">=","=>","=<","=<="],"a":">="},
{"q":"Less than?","o":["<","lt","<<","<="],"a":"<"},

# ===== DATA TYPES =====
{"q":"Stores key value?","o":["list","tuple","set","dictionary"],"a":"dictionary"},
{"q":"Unique values collection?","o":["list","tuple","set","dict"],"a":"set"},
{"q":"Ordered collection?","o":["set","dict","list","None"],"a":"list"},
{"q":"String is?","o":["Mutable","Immutable","Numeric","Boolean"],"a":"Immutable"},
{"q":"Boolean values?","o":["0/1","True/False","Yes/No","On/Off"],"a":"True/False"},
{"q":"Convert to int?","o":["str()","float()","int()","bool()"],"a":"int()"},
{"q":"Convert to string?","o":["int()","str()","chr()","repr()"],"a":"str()"},
{"q":"Length function?","o":["count()","size()","len()","length()"],"a":"len()"},
{"q":"Index starts from?","o":["0","1","-1","Depends"],"a":"0"},
{"q":"Slice operator?","o":["::","[]","{}","()"],"a":"[]"},

# ===== LOOPS =====
{"q":"Unknown iteration loop?","o":["for","while","loop","repeat"],"a":"while"},
{"q":"Stop loop keyword?","o":["end","stop","break","exit"],"a":"break"},
{"q":"Skip iteration?","o":["skip","pass","continue","next"],"a":"continue"},
{"q":"Infinite loop?","o":["while True","for True","loop True","repeat"],"a":"while True"},
{"q":"Range function used in?","o":["if","loop","for","def"],"a":"for"},
{"q":"Range start default?","o":["0","1","None","-1"],"a":"0"},
{"q":"Range step default?","o":["0","1","2","None"],"a":"1"},
{"q":"Nested loop means?","o":["loop inside loop","loop outside","no loop","double loop"],"a":"loop inside loop"},
{"q":"While loop condition?","o":["Boolean","String","Int","None"],"a":"Boolean"},
{"q":"Loop else executes when?","o":["Break","Finish normally","Error","Never"],"a":"Finish normally"},

# ===== FUNCTIONS =====
{"q":"Return keyword?","o":["give","send","return","back"],"a":"return"},
{"q":"Function without return gives?","o":["0","None","Error","True"],"a":"None"},
{"q":"Lambda is?","o":["Loop","Variable","Anonymous function","Class"],"a":"Anonymous function"},
{"q":"Arguments inside function?","o":["Parameter","Variable","Object","Module"],"a":"Parameter"},
{"q":"Default argument means?","o":["Fixed","Optional","Mandatory","None"],"a":"Optional"},
{"q":"Recursive function?","o":["Loop","Self calling","Nested","Static"],"a":"Self calling"},
{"q":"Docstring used for?","o":["Loop","Comment","Documentation","Error"],"a":"Documentation"},
{"q":"Global keyword used?","o":["Loop","Access global variable","Import","Class"],"a":"Access global variable"},
{"q":"Local variable scope?","o":["Whole program","Inside function","Outside","Module"],"a":"Inside function"},
{"q":"Pass keyword means?","o":["Stop","Continue","Do nothing","Exit"],"a":"Do nothing"},

# ===== MODULES =====
{"q":"Random number module?","o":["math","sys","random","os"],"a":"random"},
{"q":"System specific parameter module?","o":["sys","os","math","time"],"a":"sys"},
{"q":"Operating system interaction?","o":["random","os","time","sys"],"a":"os"},
{"q":"Math operations module?","o":["calc","math","num","random"],"a":"math"},
{"q":"Import keyword?","o":["include","using","import","require"],"a":"import"},
{"q":"Alias module keyword?","o":["as","alias","rename","short"],"a":"as"},
{"q":"Install packages command?","o":["pip install","python install","pkg","setup"],"a":"pip install"},
{"q":"Package manager?","o":["npm","pip","gem","apt"],"a":"pip"},
{"q":"Time delay function module?","o":["time","sys","os","random"],"a":"time"},
{"q":"Reload module function?","o":["reload","importlib.reload","load","restart"],"a":"importlib.reload"},

# ===== FILE HANDLING =====
{"q":"Open file function?","o":["file()","open()","read()","load()"],"a":"open()"},
{"q":"Read mode?","o":["w","r","a","x"],"a":"r"},
{"q":"Write mode?","o":["r","w","a","x"],"a":"w"},
{"q":"Append mode?","o":["r","w","a","x"],"a":"a"},
{"q":"Close file method?","o":["end()","stop()","close()","finish()"],"a":"close()"},
{"q":"Read full file?","o":["read()","readline()","fetch()","scan()"],"a":"read()"},
{"q":"Read one line?","o":["readline()","read()","line()","scan()"],"a":"readline()"},
{"q":"Write function?","o":["put()","write()","add()","insert()"],"a":"write()"},
{"q":"With statement purpose?","o":["Loop","File auto close","Error","Import"],"a":"File auto close"},
{"q":"File exists check module?","o":["sys","os","math","random"],"a":"os"}


]

def play_quiz():

    start_time = time.time()
    score = 0
    quiz_questions = random.sample(questions, 30)

    print(Fore.CYAN + Style.BRIGHT + "\n🎯 PYTHON QUIZ (30 QUESTIONS | 30 MIN TIMER)\n")

    for i, q in enumerate(quiz_questions, 1):

        time_spent = time.time() - start_time
        time_left = TOTAL_TIME - time_spent

        if time_left <= 0:
            print(Fore.RED + "\n⏰ TIME OVER! AUTO SUBMIT")
            break

        mins = int(time_left // 60)
        secs = int(time_left % 60)

        print(Fore.MAGENTA + f"\n⏳ Time Left: {mins}:{secs:02d}")
        print(Fore.YELLOW + f"\nQ{i}. {q['q']}")

        opts = ["A","B","C","D"]
        for opt, val in zip(opts, q["o"]):
            print(f"{opt}. {val}")

        ans = input(Fore.GREEN + "Your Answer: ").upper()

        if ans in opts:
            if q["o"][opts.index(ans)].lower() == q["a"].lower():
                print(Fore.GREEN + "✅ Correct")
                score += 1
            else:
                print(Fore.RED + f"❌ Wrong | Correct: {q['a']}")
        else:
            print(Fore.RED + "Invalid")

    percent = (score / 30) * 100

    print(Fore.CYAN + "\n🏁 QUIZ FINISHED")
    print(Fore.MAGENTA + f"⭐ Score: {score}/30")
    print(Fore.BLUE + f"📊 Percentage: {percent:.2f}%")

    if percent >= 80:
        print(Fore.GREEN + "🏆 Excellent")
    elif percent >= 50:
        print(Fore.YELLOW + "👍 Good")
    else:
        print(Fore.RED + "📚 Practice More")

while True:
    play_quiz()
    again = input("\nPlay Again? (yes/no): ")
    if again.lower() != "yes":
        print("👋 Thank you")
        break