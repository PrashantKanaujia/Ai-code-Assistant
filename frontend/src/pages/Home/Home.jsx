import { useState } from "react";

import "./Home.css";

import Sidebar from "../../components/Sidebar/Sidebar";
import QuestionBox from "../../components/QuestionBox/QuestionBox";
import AnswerPanel from "../../components/AnswerPanel/AnswerPanel";
import SourcesPanel from "../../components/SourcesPanel/SourcesPanel";
import FileViewer from "../../components/FileViewer/FileViewer";

import { getFile } from "../../services/fileService";

function Home() {

    const [selectedProject, setSelectedProject] = useState(null);
    const [answer, setAnswer] = useState(null);
    const [selectedFile, setSelectedFile] = useState(null);
    const [highlight, setHighlight] = useState(null);

    
    async function openFile(fileInfo, highlight = null) {

        try {

            const file = await getFile(
                selectedProject.id,
                fileInfo.file_path
            );

            setSelectedFile(file);
            setHighlight(highlight);


        }

        catch (error) {

            console.error(error);

        }

    }
    return (

        <div className="home">

            <Sidebar

                selectedProject={selectedProject}

                onSelectProject={setSelectedProject}

                onFileClick={openFile}

            />

            <main className="main">

                <QuestionBox
                    selectedProject={selectedProject}
                    onAnswerReceived={setAnswer}
                />

                <AnswerPanel
                    answer={answer}
                />

                <SourcesPanel
                    sources={answer?.sources || []}
                    onOpenFile={openFile}
                />

            </main>

            <FileViewer
                file={selectedFile}
                highlight={highlight}
                onClose={() => {

                setSelectedFile(null);
                setHighlight(null);

}}
            />

        </div>

    );

}

export default Home;