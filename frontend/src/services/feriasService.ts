import { api } from "./api";

export interface Ferias {
    id: string;
    colaborador_id: string;
    data_inicio: string;
    data_fim: string;
    status: string;
    observacoes: string | null;
}

export type FeriasPayload = Omit<Ferias, "id">;

export async function getFerias() {
    const { data } = await api.get<Ferias[]>("/ferias");
    return data;
}

export async function createFerias(payload: FeriasPayload) {
    const { data } = await api.post<Ferias>("/ferias", payload);
    return data;
}

export async function updateFerias(
    id: string,
    payload: Partial<FeriasPayload>
) {
    const { data } = await api.put<Ferias>(`/ferias/${id}`, payload);
    return data;
}

export async function deleteFerias(id: string) {
    await api.delete(`/ferias/${id}`);
}