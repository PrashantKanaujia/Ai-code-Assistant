import "./FileViewer.css";

import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

function FileViewer({

    file,
    source,
    onClose

}) {

    if (!file) {

        return null;

    }

    return (

        <div className="file-viewer">

            <div className="file-header">

                <h2>{file.file_name}</h2>

                <button
                    className="close-btn"
                    onClick={onClose}
                >
                    ✕
                </button>

            </div>

            <SyntaxHighlighter

                language={source?.language}

                style={oneDark}

                showLineNumbers

            >

                {file.content}

            </SyntaxHighlighter>

        </div>

    );

}

export default FileViewer;