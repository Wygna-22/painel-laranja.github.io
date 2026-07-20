import { useEffect, useState } from "react";

import type { DashboardData } from "../types/dashboard";
import { getDashboard } from "../services/dashboardService";

export function useDashboard() {
    const [dashboard, setDashboard] = useState<DashboardData | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        async function loadDashboard() {

            try {
                const data = await getDashboard();
                setDashboard(data);
            } catch (err: any) {
                console.error(err);

                setError(
                    err.response?.data?.detail ??
                    err.message ??
                    "Erro ao carregar dashboard."
                );
            } finally {

                setLoading(false);
            }

        }
        loadDashboard();

    }, []);

    return {
        dashboard,
        loading,
        error,
    };
}