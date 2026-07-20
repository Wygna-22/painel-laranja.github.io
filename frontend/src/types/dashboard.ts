export interface DashboardData {
    total_colaboradores: number;
    ativos: number;
    afastados: number;
    desligados: number;
    admissoes_mes: number;

    ferias_mes: number;
    ferias_hoje: number;

    folgas_hoje: number;
    folgas_pendentes: number;

    elogios: number;
    feedbacks: number;
    treinamentos: number;
    advertencias: number;

    por_setor: {
        setor: string;
        quantidade: number;
    }[];

    por_cidade: {
        cidade: string;
        quantidade: number;
    }[];

    ultimos_eventos: {
        colaborador: string;
        tipo: string;
        titulo: string;
        data: string;
    }[];
}