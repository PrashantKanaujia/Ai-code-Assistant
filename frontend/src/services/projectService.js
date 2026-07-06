import api from "./api";

export async function getProjects() {

    const response = await api.get("/projects");

    return response.data;
}

export async function createProject(githubUrl) {

    const response = await api.post("/projects", {
        github_url: githubUrl
    });

    return response.data;
}