from flask import Flask, render_template_string, request, session
import sqlite3
import random

app = Flask(__name__)
app.secret_key = "super_secret_key_for_sessions"

# 1. Database Setup: Creates the DB file and tables if they don't exist
def init_db():
    conn = sqlite3.connect("trivia.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trivia (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    """)
    # Check if empty, then insert a sample question
    cursor.execute("SELECT COUNT(*) FROM trivia")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO trivia (question, answer) VALUES ('What is the extension for Python files?', '.py')")
        cursor.execute("INSERT INTO trivia (question, answer) VALUES ('Which keyword creates a function?', 'def')")
        conn.commit()
    conn.close()

# 2. The Web Page Route
@app.route("/", methods=["GET", "POST"])
def game():
    init_db()
    
    # Initialize session variables if it's a new game
    if "score" not in session:
        session["score"] = 0
        conn = sqlite3.connect("trivia.db")
        cursor = conn.cursor()
        cursor.execute("SELECT question, answer FROM trivia")
        session["questions"] = cursor.fetchall() # Loads all Qs into memory
        random.shuffle(session["questions"])
        conn.close()

    feedback = ""
    
    # If the user submitted an answer
    if request.method == "POST":
        user_guess = request.form.get("guess", "").strip()
        current_q = session["questions"].pop(0) # Get the question they just answered
        
        if user_guess.lower() == current_q[1].lower():
            session["score"] += 1
            feedback = "Correct!"
        else:
            feedback = f"Wrong! The correct answer was: {current_q[1]}"
            
        session.modified = True

    # Check if game is over
    if not session["questions"]:
        final_score = session["score"]
        session.clear() # Reset for next time
        return f"<h1>Game Over! Your final score is {final_score}</h1><a href='/'>Play Again</a>"

    # Show the next question
    next_question = session["questions"][0][0]
    
    # Simple HTML interface
    html = f"""
    <h3>Score: {session['score']}</h3>
    <p>{feedback}</p>
    <h2>Question: {next_question}</h2>
    <form method="POST">
        <input type="text" name="guess" required autofocus>
        <button type="submit">Submit</button>
    </form>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)