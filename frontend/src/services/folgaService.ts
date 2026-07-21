import { api } from "./api";
import type { Folga, FolgaPayload } from "../types/folga";

export async function getFolgas() {
    const { data } = await api.get<Folga[]>("/folgas");
    return data;
}

export async function createFolga(payload: FolgaPayload) {
    const { data } = await api.post<Folga>("/folgas", payload);
    return data;
}

export async function updateFolga(
    id: string,
    payload: Partial<FolgaPayload>
) {
    const { data } = await api.put<Folga>(`/folgas/${id}`, payload);
    return data;
}

export async function deleteFolga(id: string) {
    await api.delete(`/folgas/${id}`);
}