import { useState } from "react";

import "./AddRepositoryModal.css";

import { createProject } from "../../services/projectService";

function AddRepositoryModal({
    isOpen,
    onClose,
    onRepositoryAdded
}) {

    const [githubUrl, setGithubUrl] = useState("");
    const [loading, setLoading] = useState(false);

    if (!isOpen) return null;

    async function handleAdd() {

        if (!githubUrl.trim()) {
            alert("Enter a GitHub URL.");
            return;
        }

        try {

            setLoading(true);

            await createProject(githubUrl);

            setGithubUrl("");

            onRepositoryAdded();

            onClose();

        }
        catch (error) {

            console.error(error);

            alert("Failed to add repository.");

        }
        finally {

            setLoading(false);

        }

    }

    return (

        <div className="modal-overlay">

            <div className="modal">

                <h2>Add Repository</h2>

                <input
                    type="text"
                    placeholder="https://github.com/user/repository"
                    value={githubUrl}
                    onChange={(e) => setGithubUrl(e.target.value)}
                    disabled={loading}
                />

                <div className="modal-buttons">

                    <button
                        onClick={onClose}
                        disabled={loading}
                    >
                        Cancel
                    </button>

                    <button
                        onClick={handleAdd}
                        disabled={loading}
                    >
                        {loading ? "Indexing..." : "Add"}
                    </button>

                </div>

            </div>

        </div>

    );

}

export default AddRepositoryModal;