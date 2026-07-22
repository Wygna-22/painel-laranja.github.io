import axios from "axios";

export const api = axios.create({
    baseURL: "https://painel-laranja-api.onrender.com",
});

api.interceptors.request.use((config) => {

    const token = localStorage.getItem("access_token");

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
});

export default api;