import "./AnswerPanel.css";

function AnswerPanel({ answer }) {

    return (

        <div className="answer-panel">

            <h2>Answer</h2>

            {!answer ? (

                <p className="placeholder">
                    Ask a question about the repository.
                </p>

            ) : (

                <div className="answer-content">

                    {answer.answer}

                </div>

            )}

        </div>

    );

}

export default AnswerPanel;