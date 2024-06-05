import random
import traceback
import time


studentName = "TestStudent"
inputFileName = 'ngram-sentiment.py'


problems1 = [
	["We have heard her clear, bird-like voice mingling with the scarlet symbol, and the most agreeable of his.", 
	"poetry unthrifty ignominy devoting passages ceases strewn wished concerned progenitors arrangement borne sergeants express contains flowers medicine vain mahogany social",
	"I have ever cherished, and would be convulsed with rage of grief and sob out her love for her."],
	["wealth tender spray adaptation magic view evident maidenhood them haunts pressed observing mischance wrinkles elapse mound hate mocking footpath mixture",
	"It behoves him well if he be still in my life, and the little domestic scenery of the old.",
	"And to be the father of twenty children, comprehending all perils, and the most appropriate simile."],
	["It was a being who felt himself quite astray, and the little elf whenever she hit the scarlet symbol.",
	"In the way of furniture, there was a certain depth, in a land where iniquity is dragged out into light.",
	"But, I was assured, being of mature age and infirmity, they continued, during a large part.",
	"wisdom didst piled rude predecessor accordingly granted sometimes citizen universal hand irving breathe warning convulsion unprosperous inner turn burning leading"]
] 
answers1 = [1,0,3]

problem1_trainingFile = "problem1_trainingFile.txt"

problems2 = [
	"""in , " the muse " albert brooks plays steven phillips , a hollywood screenwriter who after winning a humanitarian award for his work is dumped by his studio . 
they claim that he's lost his edge and his agent is quick to agree with them . 
he knows that he needs to write something fresh and original and quick or else his career will be over . 
so he turns to his " best " friend , jack ( jeff bridges ) another screenwriter who's enjoyed success after success . 
on the way over to jack's house steven sees jack helping an attractive woman ( sharon stone ) into a cab and begins to think : is he having an affair ? 
when confronted , jack relunctently tells him that this mystery woman is , in fact , a muse , a mythological figure who is believed to have inspired all creativity , and has helped him garner his success . 
 " she doesn't do any actual writing , " he is told , " but inspires you . " 
steven is excited by what he's hearing and asks jack to call her up to see if she'll take steven on as a new client . 
jack arranges a meeting between the two and suggests that steven bring her a present , preferably something from tiffany's . 
after the meeting the muse , sarah decides to take on steven , but at a price : she wants a suite at the four seasons and wants steven to perform odd tasks for her ( like bringing her salads in the middle of the night . ) 
steven's wife ( andy macdowell ) sees him at a food store and questions him about why he has tampons in his wagon . 
steven confesses everything and , although at first suspicious , she later allows sarah to move into their guest room and eventually into their life . 
the only question for steven is if the muse is worth all the trouble he's going through for her . 
and that's a question only time will tell . 
 " the muse " is albert brooks' sixth film as writer/director/actor ( he co-wrote with monica johnson ) and although it's a good movie it's not up to the level of his best works ( " defending your life " and " mother " ) . 
the problem lies in the script , and for a movie that relies on its dialogue for its humor , there aren't nearly as many laughs as they are chuckles despite a few good one-liners . 
it has a great premise but doesn't deliver up to it's full potential . 
but , i like albert brooks in this film and i think that we can all identify with steven phillips a little bit . 
he may whine and complain , but he just wants to support his family and be happy . 
and i like sharon stone in this movie too ; it's a nice change of pace for her . 
and i also enjoyed the cameos featuring the likes of rob reiner , james cameron and martin scorsese . 
and although " the muse " doesn't have as much to say about hollywood as robert altman's " the player " i still left the theater feeling good . 
and that's something i wish i got out of more movies . 
""",
	"""can a horror movie truly be called a horror movie if it has no scares , suspense , or even eerie elements ? 
i think not , but that's what children of the corn 666 : issac's return wants us to believe . 
the sixth installment in the horrible , worn out series is by far the worst to date . 
unlike the other five chapters , children of the corn 666 is a confusing , brainless thriller that takes the psychological horror route rather than slasher horror , but either way , none of these movies are the least bit scary . 
the film follows hannah ( natalie ramsey ) a teen looking for her mother in gatlin , nebraska , on the eve of her 21st birthday . 
what starts out as a daughter in desperate search of her long lost mother turns into the story of hannah being the first daughter of the children of the corn , who roam the cornfields looking for adults to murder . 
that's about all that's understandable in the film , as after we learn this much , issac ( john franklin ) who led the children of the corn in a previous chapter , now an older , strange man , is looking for hannah to fulfill his prophecy . 
and this is supposed to make sense . 
really . 
from the start the film is unclear of where its going , not developing any characters or throwing any concrete plot details across the table , constantly introducing new characters without personalities or the slightest hint of an individuality , and sub plots that have nothing to do with what seems to the main focus of the film . 
the film runs at a short 78 minutes , but it seems to be more in the vicinity of two hours , as the bleak , slow pacing makes children of the corn 666 : issac's return excruciatingly boring . 
plot holes are everywhere in tim sulka and john franklin's unbelievably horrible script , as nothing is accomplished or clear when the film reaches its conclusion . 
everyone and everything involved with children of the corn 666 : issac's return , namely writers john franklin and tim sulka , along with director kari skogland , should crawl under a rock , and hope no one sees their horrible work of trash . 
the bottom line : horrible , horrible , horrible . 
another attempt to revive this worn out genre falls flat . 
and what's with that title ? 
the devil has nothing to do whatsoever with this film . 
let's pray that this is the finale in one of the worst current film series . 
one of the worst horror films in years . 
"""
]
answers2 = [True, False]	
problem2_trainingFile = "problem2_trainingFile.jsonlist"

"""problem2 is graded based on what fraction of the test set you get correct. If you get baselineCorrect, then you get 0 points for problem 2. If you get maxCorrect, you get 50 points (full credit). You can earn up to 60 (out of 50) points for this problem.
"""
baselineCorrect = 0.5
maxCorrect = 0.65

# maxProblemTimeout = 30


outFile = open("grade_"+studentName+".txt", 'w')

def prnt(S):
	global outFile
	outFile.write(str(S) + "\n")
	print(S)

try:
	F = open(inputFileName, 'r', encoding="utf-8")
	exec("".join(F.readlines()))
except Exception as e:
	prnt("Couldn't open or execute '" + inputFileName + "': " + str(traceback.format_exc()))
	prnt("FINAL SCORE: 0")
	exit()


p1score = 50
#PROBLEM 1
prnt('='*30)
try:
	prnt("CALLING YOUR calcNGrams_train FUNCTION")
	startTime = time.time()
	calcNGrams_train(problem1_trainingFile)
	endTime = time.time()
except Exception as e:
	endTime = time.time()
	prnt("\tError arose: " + str(traceback.format_exc()))
# 		currentScore -= 10*len(problems1)
	prnt("\tNOTE: We won't penalize you directly for this, but this is likely to lead to exceptions later.")	
if endTime - startTime > 120:
	prnt("Time to execute was " + str(int(endTime-startTime)) + " seconds; this is too long (-10 points)")
	p1score -= 10
for i in range(len(problems1)):
	P = problems1[i]
	A = answers1[i]
	
	prnt("\n\nTESTING ON INPUT PROBLEM:")
	prnt(P)
	prnt("CORRECT OUTPUT:")
	prnt(str(A))
	prnt("YOUR OUTPUT:")
	try:
		startTime = time.time()
		result = calcNGrams_test(P)
		prnt(result)
		endTime = time.time()		
		if endTime-startTime > 120:
			prnt("Time to execute was " + str(int(endTime-startTime)) + " seconds; this is too long (-10 points)")
		elif result==A:
			prnt("Correct!")
		else:
			prnt("Incorrect (-10 points)")
			p1score -= 10

	except Exception as e:
		prnt("Error while executing this problem: " + str(traceback.format_exc()))
		p1score -= 10
p1score = max(p1score, 0)

#PROBLEM 2
p2score = 0
prnt('='*30)
try:
	prnt("CALLING YOUR calcSentiment_train FUNCTION")
	startTime = time.time()
	calcSentiment_train(problem2_trainingFile)
	endTime = time.time()
except Exception as e:
	endTime = time.time()
	prnt("\tError arose: " + str(traceback.format_exc()))
# 		currentScore -= 10*len(problems1)
	prnt("\tNOTE: We won't penalize you directly for this, but this is likely to lead to exceptions later.")
if endTime - startTime > 120:
	prnt("Time to execute was " + str(int(endTime-startTime)) + " seconds; this is too long (-10 points)")
	p2score -= 10
numCorrect = 0
for i in range(len(problems2)):
	P = problems2[i]
	A = answers2[i]
	
	prnt("\n\nTESTING ON INPUT PROBLEM:")
	prnt(P)
	prnt("CORRECT OUTPUT:")
	prnt(str(A))
	prnt("YOUR OUTPUT:")
	try:
		startTime = time.time()
		result = calcSentiment_test(P)
		prnt(result)
		endTime = time.time()		
		if endTime-startTime > 120:
			prnt("Time to execute was " + str(int(endTime-startTime)) + " seconds; this is too long (marked as wrong)")
		elif result==A:
			prnt("Correct!")
			numCorrect += 1
		else:
			prnt("Incorrect")

	except Exception as e:
		prnt("Error while executing this problem: " + str(traceback.format_exc()))
percentCorrect = numCorrect*1.0/len(problems2)
points = min(60, 50 * (percentCorrect - baselineCorrect) / (maxCorrect - baselineCorrect))
prnt("\nYou got " + str(percentCorrect*100) + "% correct: +" + str(points) + "/50 points")
p2score =+ points
p2score = max(p2score, 0)

prnt('='*30)
prnt('='*30)
prnt('='*30)
prnt("FINAL SCORE:" + str(p1score + p2score))