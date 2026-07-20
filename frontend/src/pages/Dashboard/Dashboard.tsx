import DashboardLayout from "../../components/DashboardLayout/DashboardLayout";
import DashboardGrid from "../../components/DashboardGrid/DashboardGrid";
import ChartsGrid from "../../components/ChartsGrid/ChartsGrid";
import ChartCard from "../../components/ChartCard/ChartCard";

import CollaboratorsChart from "../../components/Charts/CollaboratorsChart";
import StatusChart from "../../components/Charts/StatusChart";
import KpiCard from "../../components/KpiCard/KpiCard";

import { useDashboard } from "../../hooks/useDashboard";

import {
    Users,
    CalendarDays,
    CalendarCheck,
    UserCog,
} from "lucide-react";

export default function Dashboard() {

    const {
        dashboard,
        loading,
        error,
    } = useDashboard();

    if (loading) {
        return (
            <DashboardLayout>
                <h2>Carregando dashboard...</h2>
            </DashboardLayout>
        );
    }

    if (error) {
        return (
            <DashboardLayout>
                <h2>Erro ao carregar dashboard</h2>
                <p>{error}</p>
            </DashboardLayout>
        );
    }

    return (
        <DashboardLayout>

            <div>
                <h1>Dashboard</h1>

                <p
                    style={{
                        color: "#64748B",
                        marginTop: 8,
                    }}
                >
                    Resumo geral do Painel Laranja.
                </p>
            </div>

            <DashboardGrid>

                <KpiCard
                    title="Colaboradores"
                    value={dashboard?.total_colaboradores ?? 0}
                    color="#3B82F6"
                    icon={<Users size={28} />}
                />

                <KpiCard
                    title="Em férias"
                    value={dashboard?.ferias_hoje ?? 0}
                    color="#22C55E"
                    icon={<CalendarDays size={28} />}
                />

                <KpiCard
                    title="Folgas hoje"
                    value={dashboard?.folgas_hoje ?? 0}
                    color="#F97316"
                    icon={<CalendarCheck size={28} />}
                />

                <KpiCard
                    title="Ativos"
                    value={dashboard?.ativos ?? 0}
                    color="#A855F7"
                    icon={<UserCog size={28} />}
                />

            </DashboardGrid>

            <ChartsGrid>

                <ChartCard title="Colaboradores por setor">
                    <CollaboratorsChart
                        data={dashboard?.por_setor ?? []}
                    />
                </ChartCard>

                <ChartCard title="Status geral">
                    <StatusChart
                        ativos={dashboard?.ativos ?? 0}
                        afastados={dashboard?.afastados ?? 0}
                        desligados={dashboard?.desligados ?? 0}
                    />
                </ChartCard>

            </ChartsGrid>

        </DashboardLayout>
    );
}