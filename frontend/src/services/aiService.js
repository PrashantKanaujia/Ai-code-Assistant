import api from "./api";

export async function askQuestion(projectId, question) {

    const response = await api.post("/ask", {
        project_id: projectId,
        question: question
    });

    return response.data;
}