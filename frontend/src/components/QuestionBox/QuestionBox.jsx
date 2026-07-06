import { useState } from "react";
import "./QuestionBox.css";

import { askQuestion } from "../../services/aiService";

function QuestionBox({
    selectedProject,
    onAnswerReceived
}) {

    const [question, setQuestion] = useState("");
    const [loading, setLoading] = useState(false);

    async function handleAsk() {

        if (!selectedProject) {
            alert("Please select a repository.");
            return;
        }

        if (!question.trim()) {
            alert("Please enter a question.");
            return;
        }

        try {

            setLoading(true);

            const response = await askQuestion(
                selectedProject.id,
                question
            );

            onAnswerReceived(response);

        } catch (error) {

            console.error(error);
            alert("Failed to get AI response.");

        } finally {

            setLoading(false);

        }

    }

    return (

        <div className="question-box">

            <textarea
                placeholder="Ask anything about the repository..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />

            <button
                onClick={handleAsk}
                disabled={loading}
            >
                {loading ? "Thinking..." : "Ask"}
            </button>

        </div>

    );

}

export default QuestionBox;