import { api } from "./api";

interface LoginData {
    username: string;
    password: string;
}

export async function login(data: LoginData) {

    const form = new URLSearchParams();

    form.append("username", data.username);
    form.append("password", data.password);

    const response = await api.post(
        "/auth/login",
        form,
        {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        }
    );

    localStorage.setItem(
        "access_token",
        response.data.access_token
    );

    return response.data;
}

export function logout() {
    localStorage.removeItem("access_token");
}

export function getToken() {
    return localStorage.getItem("access_token");
}

export function isAuthenticated() {
    return !!getToken();
}