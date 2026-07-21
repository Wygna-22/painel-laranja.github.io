import { useEffect, useState } from "react";

import type {
    Ferias,
    FeriasPayload,
} from "../services/feriasService";

import {
    getFerias,
    createFerias,
    updateFerias,
    deleteFerias,
} from "../services/feriasService";

export function useFerias() {

    const [ferias, setFerias] = useState<Ferias[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    async function load() {

        try {

            setLoading(true);

            const data = await getFerias();

            setFerias(data);

            setError("");

        } catch {

            setError("Erro ao carregar férias.");

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {
        load();
    }, []);

    async function create(data: FeriasPayload) {

        await createFerias(data);

        await load();

    }

    async function update(id: string, data: Partial<FeriasPayload>) {

        await updateFerias(id, data);

        await load();

    }

    async function remove(id: string) {

        await deleteFerias(id);

        await load();

    }

    return {
        ferias,
        loading,
        error,
        reload: load,
        create,
        update,
        remove,
    };
}