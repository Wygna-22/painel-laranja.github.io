import { api } from "./api";
import type { Gestor } from "../types/gestor";

export async function getGestores(): Promise<Gestor[]> {
    const response = await api.get("/gestores");
    return response.data;
}

export async function createGestor(
    data: Omit<Gestor, "id">
) {
    const response = await api.post("/gestores", data);
    return response.data;
}

export async function updateGestor(
    id: string,
    data: Partial<Gestor>
) {
    const response = await api.put(`/gestores/${id}`, data);
    return response.data;
}

export async function deleteGestor(id: string) {
    await api.delete(`/gestores/${id}`);
}