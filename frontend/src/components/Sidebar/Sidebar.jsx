import { useEffect, useState } from "react";

import "./Sidebar.css";

import { getProjects } from "../../services/projectService";
import { getRepositoryFiles } from "../../services/repositoryService";

import AddRepositoryModal from "../AddRepositoryModal/AddRepositoryModal";

function Sidebar({ selectedProject, onSelectProject }) {

    const [projects, setProjects] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [showModal, setShowModal] = useState(false);
    const [files, setFiles] = useState([]);

    async function selectProject(project) {

    onSelectProject(project);

    try {

        const repositoryFiles = await getRepositoryFiles(
            project.id
        );

        setFiles(repositoryFiles);

    }

    catch(error){

        console.error(error);

    }

}


    async function loadProjects() {

        try {

            const data = await getProjects();

            setProjects(data);

        } catch (err) {

            console.error(err);
            setError("Failed to load repositories.");

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {

        loadProjects();

    }, []);

    return (

        <aside className="sidebar">

            <h1>AI Repository Engineer</h1>

            <h2>Repositories</h2>

            {loading && (
                <p>Loading repositories...</p>
            )}

            {error && (
                <p>{error}</p>
            )}

            {!loading && !error && (

                <div className="repo-list">

                    {projects.map((project) => (

                        <button
                            key={project.id}
                            className={
                                selectedProject?.id === project.id
                                    ? "repo-item active"
                                    : "repo-item"
                            }
                            onClick={() => selectProject(project)}
                        >
                            {project.name}
                            <div className="file-list">

                            {
                                files.map((file,index)=>(

                                    <div key={index}>
                                        {file.path}
                                    </div>

                                ))
                            }

                            </div>
                        </button>

                    ))}

                </div>

            )}
            
            <button
                className="add-btn"
                onClick={() => setShowModal(true)}
            >
                + Add Repository
            </button>

            <AddRepositoryModal
                isOpen={showModal}
                onClose={() => setShowModal(false)}
                onRepositoryAdded={loadProjects}
            />

        </aside>

    );

}

export default Sidebar;