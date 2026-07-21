export interface Folga {
    id: string;
    colaborador_id: string;
    data: string;
    status: string;
    motivo: string;
    observacoes: string | null;
}

export type FolgaPayload = Omit<Folga, "id">;