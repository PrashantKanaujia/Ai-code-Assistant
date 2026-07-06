import api from "./api";


export async function getRepositoryFiles(projectId) {

    const response = await api.get(
        `/projects/${projectId}/files`
    );

    return response.data;

}