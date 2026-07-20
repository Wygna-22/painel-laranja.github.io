import { api } from "./api";
import type { Colaborador } from "../types/colaborador";

export async function getColaboradores(): Promise<Colaborador[]> {
    const response = await api.get("/colaboradores");
    return response.data;
}

export async function createColaborador(
    data: Omit<Colaborador, "id">
) {
    const response = await api.post("/colaboradores", data);
    return response.data;
}

export async function updateColaborador(
    id: string,
    data: Partial<Colaborador>
) {
    const response = await api.put(`/colaboradores/${id}`, data);
    return response.data;
}

export async function deleteColaborador(id: string) {
    await api.delete(`/colaboradores/${id}`);
}