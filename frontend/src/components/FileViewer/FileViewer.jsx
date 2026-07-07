import "./FileViewer.css";
import { useEffect, useRef } from "react";

import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";
// import { atomDark } from "react-syntax-highlighter/dist/esm/styles/prism";
// import { vscDarkPlus } from "react-syntax-highlighter/dist/esm/styles/prism";
// import { dracula } from "react-syntax-highlighter/dist/esm/styles/prism";
// import { nightOwl } from "react-syntax-highlighter/dist/esm/styles/prism";


function FileViewer({

    file,
    highlight,
    onClose

}){
    const codeContainerRef = useRef(null);
    useEffect(() => {

    if (!highlight)
        return;

    const line = document.getElementById(

        `line-${highlight.start_line}`

    );

    if (line) {

        line.scrollIntoView({

            behavior: "smooth",

            block: "center"

        });

    }

}, [highlight, file]);

    if (!file) {

        return null;

    }
    // console.log(source)
    // console.log(file)


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

            <div
    className="code-container"
    ref={codeContainerRef}
>

    <SyntaxHighlighter

        language={file.language}

        style={oneDark}

        showLineNumbers

        wrapLines

        lineProps={(lineNumber) => {

            const selected =

                highlight &&

                lineNumber >= highlight.start_line &&

                lineNumber <= highlight.end_line;

            return {

                id: `line-${lineNumber}`,

                style: {

                    display: "block",

                    backgroundColor: selected
                        ? "#3b4252"
                        : "transparent"

                }

            };

        }}

    >

        {file.content}

    </SyntaxHighlighter>

</div>

        </div>

    );

}

export default FileViewer;