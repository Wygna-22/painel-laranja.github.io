import { api } from "./api";

export interface Indicador {
    id: string;
    user_id: string;
    mes: number;
    ano: number;
    qtd_pessoas: number;
    dias_atual: number;
    dias_mes: number;
    pontos: number;
    ppc: number;
    meta_ppc: number;
    falta_meta_dia: number;
    meta_mes: number;
    esperado_atual: number;
    falta_meta_mes: number;
}

export type IndicadorCreate = Omit<Indicador, "id">;
export async function getIndicadores() {
    const response = await api.get<Indicador[]>(
        "/indicadores/"
    );

    return response.data;
}

export async function getIndicador(id: string) {
    const response = await api.get<Indicador>(
        `/indicadores/${id}`
    );

    return response.data;
}

export async function createIndicador(
    data: IndicadorCreate
) {
    const response = await api.post(
        "/indicadores/",
        data
    );

    return response.data;
}

export async function updateIndicador(
    id: string,
    data: Partial<IndicadorCreate>,
) {

    const response = await api.put(
        `/indicadores/${id}`,
        data,
    );

    return response.data;
}

export async function deleteIndicador(
    id: string,
) {

    await api.delete(
        `/indicadores/${id}`,
    );
}