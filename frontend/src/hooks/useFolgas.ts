import { useEffect, useState } from "react";

import type {
    Folga,
    FolgaPayload,
} from "../types/folga";

import {
    getFolgas,
    createFolga,
    updateFolga,
    deleteFolga,
} from "../services/folgaService";

export function useFolgas() {

    const [folgas, setFolgas] = useState<Folga[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    async function load() {

        try {

            setLoading(true);

            const data = await getFolgas();

            setFolgas(data);

            setError("");

        } catch {

            setError("Erro ao carregar folgas.");

        } finally {

            setLoading(false);

        }

    }

    useEffect(() => {
        load();
    }, []);

    async function create(data: FolgaPayload) {

        await createFolga(data);

        await load();

    }

    async function update(
        id: string,
        data: Partial<FolgaPayload>
    ) {

        await updateFolga(id, data);

        await load();

    }

    async function remove(id: string) {

        await deleteFolga(id);

        await load();

    }

    return {
        folgas,
        loading,
        error,
        reload: load,
        create,
        update,
        remove,
    };
}