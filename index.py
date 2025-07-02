import streamlit as st
import random

def generate_blog(topic):
    titles = [
        f"Mastering {topic} in Simple Steps",
        f"Your Ultimate Guide to {topic}",
        f"Everything You Need to Know About {topic}",
        f"Top 5 {topic} Trends to Watch in 2025",
        f"How {topic} is Changing the Game",
        f"Unlocking the Secrets of {topic}",
        f"Why You Should Start Learning {topic} Today",
        f"10 Surprising Facts About {topic}",
        f"How to Excel at {topic} in 2025",
        f"The Future of {topic}: What to Expect",
        f"Getting Started with {topic}: A Beginner's Guide",
        f"Advanced Techniques in {topic} You Should Know",
        f"Common Mistakes in {topic} and How to Avoid Them",
        f"How to Stay Ahead in {topic} This Year",
        f"Essential Tools for Mastering {topic}",
        f"From Novice to Expert: Your Journey in {topic}",
        f"Exploring the Benefits of {topic}",
        f"How {topic} Can Boost Your Career",
        f"Top Resources for Learning {topic}",
        f"How to Integrate {topic} into Your Daily Routine",
        f"Understanding the Basics of {topic}",
        f"5 Myths About {topic} Debunked",
        f"How to Overcome Challenges in {topic}",
        f"Future-Proofing Your Skills with {topic}",
        f"Essential {topic} Skills for 2025",
        f"How to Leverage {topic} for Success",
        f"Why {topic} is the Key to Innovation",        
        f"Unlocking the Power of {topic} in Your Career",
        f"Why {topic} Matters in 2025",
        f"The Power of {topic}: Explained!",
        f"Mastering the art of {topic}",
        f"why {topic} is the skill everyone should learn",
        f"Exploring the Future of {topic}",
        f"The Ultimate Guide to {topic}",
        f"{topic} for Beginners: Start Smart",
        f"What No One Tells You About {topic}",
        f"How {topic} Can Change the Way You Work",
        f"Getting Started with {topic}. A Quick Guide",
        f"Is {topic} Really Worth Your Time?",
        f"The Hidden Truths Behind {topic}",
        f"Everything You Need to Know About {topic}",
        f"7 Ways to Get Better at {topic}",
        f"How I Improved at {topic} in Just One Month",
        f"A Simple Approach to Understanding {topic}",
        f"{topic}: Mindset, Strategy & Execution",
        f"Mistakes to Avoid While Learning {topic}",
        f"A Step-by-Step Plan to Master {topic}",
        f"Don’t Start {topic} Until You Read This",
        f"How {topic} Connects with the Real World",
        f"Writing About {topic} Tips for Creators",
        f"How {topic} Can Boost Your Career",
        f"{topic} Ideas You Haven’t Thought of Yet",
        f"Tools & Resources to Learn {topic} Faster",
        f"The Evolution of {topic} Over Time",
        f"The Future of {topic} — Trends to Watch",
        f"What Experts Say About {topic}",
        f"How {topic} Is Used Around the World",
        f"Navigating the World of {topic} as a Beginner",
        f"The Language of {topic} – Explained",
        f"How to Make {topic} Fun & Engaging",
        f"10 Quick Facts About {topic} You Must Know",
        f"Essential {topic} Skills for 2025",
        f"How to Leverage {topic} for Success",
        f"Why {topic} is the Key to Innovation",        
        f"Unlocking the Power of {topic} in Your Career",
        f"Why {topic} Matters in 2025",
        f"The Power of {topic}: Explained!"
        f"{topic} Tips You Need to Know Today"
    ]


    intros = [
        f"In today's fast-paced world, {topic} has become essential.",
        f"{topic} is not just a skill — it's a necessity in modern life.",
        f"From beginners to pros, {topic} helps everyone grow.",
        f"If you're curious about {topic}, you're not alone.",
        f"{topic} can unlock powerful opportunities — let's explore how."
        f"In today's fast-paced world, {topic} has become essential.",
        f"{topic} is not just a skill — it's a necessity in modern life.",
        f"From beginners to pros, {topic} helps everyone grow.",
        f"If you're curious about {topic}, you're not alone.",
        f"{topic} can unlock powerful opportunities — let's explore how.",
        f"Whether you're a student, creator, or professional, {topic} can take your journey to the next level.",
        f"Have you ever wondered how {topic} fits into your daily life? You're about to find out.",
        f"{topic} is more than a buzzword — it’s a mindset, a tool, and a superpower.",
        f"The world is changing fast — and {topic} is right at the center of it.",
        f"Exploring {topic} is like opening a door to endless possibilities.",
        f"In a world full of distractions, {topic} helps you stay focused and future-ready.",
        f"Whether you're building a career or a passion project, {topic} has your back.",
        f"{topic} might just be the skill you didn’t know you needed — until now.",
        f"Let’s dive into why {topic} is capturing attention everywhere.",
        f"{topic} is where innovation meets impact — and it's easier to start than you think.",
        f"If you're thinking about diving into {topic}, this is your sign to begin.",
        f"{topic} isn't just a skill — it's a way of thinking and creating.",
        f"No matter your background, {topic} can help you express, grow, and succeed.",
        f"Your next breakthrough might just begin with {topic}.",
        f"In every corner of life — work, creativity, or learning — {topic} has value.",
        f"Whether you want to earn, learn, or explore, {topic} can be your toolkit.",
        f"Mastering {topic} doesn’t require perfection — just a curious mind.",
        f"The future belongs to the curious — and {topic} rewards those who start early.",
        f"{topic} has quietly become one of the most powerful tools of our time.",
        f"The more you explore {topic}, the more you'll realize its potential.",
        f"In an age of creators and problem-solvers, {topic} sits right at the center.",
        f"{topic} is transforming how we work, think, and connect — and this is your entry point.",
        f"Learning {topic} today means unlocking new doors tomorrow.",
        f"Think {topic} is complex? Let’s break it down, step by step.",
        f"From side-hustles to personal growth — {topic} can shape it all.",
        f"Curiosity is the first step, and {topic} makes the journey worth it.",
        f"Whether you’re starting from scratch or leveling up — {topic} will meet you where you are.",
        f"{topic} empowers you to create, connect, and contribute in ways that matter.",
        f"Every expert was once a beginner — let {topic} be your next starting line.",
        f"{topic} may sound intimidating, but it’s surprisingly fun once you start.",
        f"What makes {topic} so exciting is that it grows with you.",
        f"{topic} is one of those rare things that blends logic and creativity.",
        f"You don’t need years of experience — just a spark of curiosity about {topic}.",
        f"Once you understand {topic}, you’ll see opportunities everywhere.",
        f"{topic} can turn an ordinary idea into something impactful and alive.",
        f"Let’s take a fresh, simple look at how {topic} fits into real life.",
        f"In 2025 and beyond, {topic} is becoming a life skill, not just a niche.",
        f"You’ve heard about {topic}, but what does it really mean for you?",
        f"Even 10 minutes a day with {topic} can make a huge difference.",
        f"{topic} is not just for techies — it's for thinkers, creators, and doers too.",
        f"With the rise of AI, creativity, and remote work — {topic} is more relevant than ever.",
        f"The internet is filled with noise — but {topic} helps you create meaning.",
        f"Let’s simplify {topic} so it feels less overwhelming — and more empowering.",
        f"{topic} bridges the gap between your ideas and your goals.",
        f"It’s not about mastering everything — just start with one step in {topic}.",
        f"Some people fear the future — others prepare with {topic}.",
        f"Ever felt stuck? {topic} might just be your escape button.",
        f"In a world of fast scrolls, {topic} helps you slow down and build something lasting.",
        f"Many great things begin with a notebook, a laptop — and a bit of {topic}.",
        f"Don't wait for the perfect moment — let {topic} be your starting point today."     
    ]


    tips = [
        "Start small — you don’t need to master everything on day one.",
        "Be consistent, even if progress feels slow.",
        "Keep a notebook or digital log of what you learn.",
        "Learn by doing — theory is just the beginning.",
        "Make mistakes — that’s how real growth happens.",
        "Follow people already doing great work in this space.",
        "Don’t compare your chapter 1 to someone’s chapter 10.",
        "Break big tasks into smaller, doable chunks.",
        "Use free resources — they’re everywhere!",
        "Teach what you learn — it helps you remember.",
        "Find a routine that works for YOU, not the internet.",
        "Track your progress weekly — it’ll keep you motivated.",
        "Say yes to challenges — they’ll speed up your learning.",
        "Use templates and frameworks to save time.",
        "Don’t chase perfection — chase progress.",
        "Collaborate with others — you’ll grow faster.",
        "Ask questions, even if they feel basic.",
        "Keep things fun — mix in creativity whenever you can.",
        "Reward yourself for milestones — even small ones!",
        "Use tools that make your life easier.",
        "Sleep on your drafts — clarity comes the next day.",
        "Revisit old work to see how far you’ve come.",
        "Be patient — it’s okay to not ‘get it’ immediately.",
        "Join communities related to your topic.",
        "Create before you consume — even if it’s messy.",
        "Batch your learning sessions to avoid burnout.",
        "Don’t hoard tutorials — apply what you learn.",
        "Try different learning formats: videos, books, blogs.",
        "Experiment — you’ll discover new ideas.",
        "Focus on depth, not just speed.",
        "Stay inspired — follow creators who excite you.",
        "Delete distractions during deep work.",
        "If you're stuck, switch up your environment.",
        "Avoid burnout — rest is also productive.",
        "Celebrate every tiny win.",
        "Let curiosity lead you — it’s the best compass.",
        "Ask 'why' more often — dig deeper.",
        "Use checklists — they reduce stress.",
        "Reflect weekly on what worked and what didn’t.",
        "You don’t need to know everything to start today."
    ]


    outros = [
        f"Thanks for reading! Hope this gave you a fresh perspective on {topic}.",
        f"Whether you're just starting out or deep into {topic}, keep exploring!",
        f"If you found this helpful, feel free to share it with someone who needs it.",
        f"Stay curious, keep learning, and don’t stop experimenting with {topic}.",
        f"Let’s continue the conversation — what’s your take on {topic}?",    
        f"Hope you’re walking away with something useful — or at least inspired 🧠✨",
        f"Until next time — stay kind, stay creative, and keep growing 🌱",
        f"If this sparked your interest in {topic}, don’t let it fade — take the next step!",
        f"The best way to learn more about {topic}? Start doing it.",
        f"Got thoughts or questions? Drop them below or reach out — let’s connect!",
        f"Don’t let this be just another read — turn it into action 🛠️",
        f"Thanks for being here — your curiosity means the world 🌍",
        f"If this helped you, imagine who else it could help — go ahead and share ✨",
        f"Learning is a journey — and {topic} is an amazing part of it.",
        f"Now that you know the basics, where will you take {topic} next?",
        f"This is your sign to *start* — even if it’s messy, just begin.",
        f"Want more content like this? Stay tuned, there’s always more coming 🔄",
        f"If this resonated with you — don’t forget to bookmark or share ❤️",
        f"Step by step, you'll get better at {topic} — trust the process.",
        f"Catch you in the next post — with more ideas, insights, and maybe caffeine ☕",
        f"Feel free to explore more — the world of {topic} is vast and exciting 🌐",
        f"Thanks for reading till the end — you’re awesome 💪",
        f"Big or small, every step you take in {topic} counts.",
        f"Time to apply this — even the tiniest action makes progress 🌟",
        f"PS: Don’t just scroll, start doing. That’s where growth lives.",
        f"Keep showing up — even on the hard days. That’s how you grow.",
        f"Hope this was helpful — and maybe a little fun too 💫",
        f"Until next time — stay passionate, stay playful 🌈",
        f"Want more resources around {topic}? Let me know, I got you!",
        f"If you loved this, consider sharing it — let good content travel 📤",
        f"This journey is just beginning — where will you go with {topic}?",
        f"You’re more ready than you think — just start 🌸",
        f"Learning never ends — especially with something as rich as {topic}.",
        f"Reading is great — but real magic happens when you take the next step.",
        f"Your future self will thank you for starting today 💌",
        f"I’d love to hear your thoughts — how do *you* use {topic}?",
        f"Remember: consistency > perfection. Especially in {topic}.",
        f"Thanks for sticking around till the end — let’s grow together 🌿",
        f"Keep learning, keep writing, keep evolving ✍️⚙️",
        f"Go on — take that tiny bold step toward mastering {topic}."
    ]
    return random.choice(titles), random.choice(intros), random.sample(tips, 3), random.sample(outros, 2)


st.title("Blog Writing Assistant 📝")
st.markdown(
    """
    <style>
    @media (prefers-color-scheme: light) {
        .stApp {
            background-color: #FBCEB1;
            color: #1a1a1a; 
        }

        header[data-testid="stHeader"] {
            background-color: #FFBEA7; 
        }

        .stButton>button {
            background-color: #fb923c; /* peachy orange */
        }
    }

    @media (prefers-color-scheme: dark) {
        .stApp {
            background-color: #871111; 
            color: #FFBEA7;
        }

        header[data-testid="stHeader"] {
            background-color: #9F2929; 
        }

        .stButton>button {
            background-color: #9F2929; 
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.write("Enter a topic and get a quick blog starter ✨")

topic = st.text_input("Enter your blog topic:")

if st.button("Generate Blog Ideas"):
    if topic:
        title, intro, points, outros = generate_blog(topic)

        st.subheader("📰 Blog Title:")
        st.success(title)



        st.subheader("📜 Introduction:")
        st.info(intro)

        st.subheader("📌 Key Tips:")
        for point in points:
            st.markdown(f"- {point}")

        st.subheader("💬 Outro Ideas:")
        for outro in outros:
            st.markdown(f"- {outro}")

        st.success("Happy writing! 🎉")
    else:
        st.warning("Please enter a topic first.")



st.markdown("<hr>", unsafe_allow_html=True)
st.write("**From brain ➜ to code ➜ to screen ✨ ------  by Palwashey :)**")