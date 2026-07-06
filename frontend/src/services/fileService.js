import api from "./api";

export async function getFile(projectId, filePath) {

    const response = await api.get(
        `/projects/${projectId}/file`,
        {
            params: {
                path: filePath
            }
        }
    );

    return response.data;

}