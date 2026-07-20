import { useEffect, useState } from "react";

import type { Colaborador } from "../types/colaborador";

import {
    getColaboradores,
    createColaborador,
    updateColaborador,
    deleteColaborador,
} from "../services/colaboradorService";

export function useColaboradores() {

    const [colaboradores, setColaboradores] = useState<Colaborador[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    async function reload() {
        try {

            setLoading(true);

            const data = await getColaboradores();

            setColaboradores(data);

        } catch {

            setError("Erro ao carregar colaboradores.");

        } finally {

            setLoading(false);

        }
    }

    async function create(data: Omit<Colaborador, "id">) {

        await createColaborador(data);

        await reload();

    }

    async function update(id: string, data: Partial<Colaborador>) {

        await updateColaborador(id, data);

        await reload();

    }

    async function remove(id: string) {

        await deleteColaborador(id);

        await reload();

    }

    useEffect(() => {

        reload();

    }, []);

    return {

        colaboradores,

        loading,

        error,

        reload,

        create,

        update,

        remove,

    };

}