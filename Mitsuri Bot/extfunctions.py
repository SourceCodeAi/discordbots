import random



truths = [
        "When was the last time you lied?",
        "When was the last time you lied?",
        "When was the last time you cried?",
        "What's your biggest fear?",
        "What's your biggest fantasy?",
        "Do you have any fetishes?",
        "What's something you're glad your mum doesn't know about you?",
        "Have you ever cheated on someone?",
        "What's the worst thing you've ever done?",
        "What's a secret you've never told anyone?",
        "Do you have a hidden talent?",
        "Who was your first celebrity crush?",
        "What are your thoughts on polyamory?",
        "Have you ever cheated in an exam?",
        "What's the most drunk you've ever been?",
        "Have you ever broken the law?",
        "What's the most embarrassing thing you've ever done?",
        "What's your biggest insecurity?",
        "What's the biggest mistake you've ever made?",
        "What's the most disgusting thing you've ever done?",
        "Who would you like to kiss in this server?",
        "What's the worst thing anyone's ever done to you?",
        "Have you ever had a run in with the law?",
        "What's your worst habit?",
        "What's the worst thing you've ever said to anyone?",
        "Have you ever peed in the shower?",
        "What's the strangest dream you've had?",
        "Have you ever been caught doing something you shouldn't have?",
        "What's the worst date you've been on?",
        "What's your biggest regret?",
        "What's the biggest misconception about you?",
        "Why did your last relationship break down?",
        "Have you ever lied to get out of a bad date?",
        "What's the most trouble you've been in? "
]

dares = [
        "Show the most embarrassing photo on your phone",
        "Show the last five people you texted and what the messages said",
        "Let the rest of the group DM someone from your Instagram account",
        "Eat a raw piece of garlic",
        "Do 100 squats",
        "Keep three ice cubes in your mouth until they melt",
        "Say something dirty to the person on your left",
        "Give a foot massage to the person on your right",
        "Put 10 different available liquids into a cup and drink it",
        "Yell out the first word that comes to your mind",
        "Give a lap dance to someone of your choice",
        "Like the first 15 posts on your Facebook newsfeed",
        "Eat a spoonful of mustard",
        "Keep your eyes closed until it's your go again",
        "Seductively eat a banana",
        "Empty out your wallet/purse and show everyone what's inside",
        "Pretend to be the person to your right for 10 minutes",
        "Eat a snack without using your hands",
        "Say two honest things about everyone else in the group",
        "Twerk for a minute",
        "Try and make the group laugh as quickly as possible",
        "Try to put your whole fist in your mouth",
        "Tell everyone an embarrassing story about yourself",
        "Try to lick your elbow",
        "Post the oldest selfie on your phone on Instagram Stories",
        "Tell the saddest story you know",
        "Howl like a wolf for two minutes",
        "Dance without music for two minutes",
        "Pole dance with an imaginary pole",
        "Let someone else tickle you and try not to laugh",
        "Put as many snacks into your mouth at once as you can "
]

def choose_truth():
    truth = random.choice(truths)
    return truth



def choose_dare():
    dare = random.choice(dares)
    return dare

