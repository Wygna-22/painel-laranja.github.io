import DashboardLayout from "../../components/DashboardLayout/DashboardLayout";
import DashboardGrid from "../../components/DashboardGrid/DashboardGrid";
import ChartsGrid from "../../components/ChartsGrid/ChartsGrid";
import ChartCard from "../../components/ChartCard/ChartCard";

import CollaboratorsChart from "../../components/Charts/CollaboratorsChart";
import StatusChart from "../../components/Charts/StatusChart";

import {
  Users,
  CalendarDays,
  CalendarCheck,
  UserCog,
} from "lucide-react";

import KpiCard from "../../components/KpiCard/KpiCard";

// ... imports dos KPIs

export default function Dashboard() {
    return (
        <DashboardLayout>

            <div>
                <h1>Dashboard</h1>
                <p
                    style={{
                        color: "#64748B",
                        marginTop: 8
                    }}
                >
                    Resumo geral do Painel Laranja.
                </p>
            </div>

            <DashboardGrid>

                <KpiCard
                    title="Colaboradores"
                    value={182}
                    color="#3B82F6"
                    icon={<Users size={28} />}
                />

                <KpiCard
                    title="Em Férias"
                    value={12}
                    color="#22C55E"
                    icon={<CalendarDays size={28} />}
                />

                <KpiCard
                    title="Folgas Hoje"
                    value={18}
                    color="#F97316"
                    icon={<CalendarCheck size={28} />}
                />

                <KpiCard
                    title="Gestores"
                    value={15}
                    color="#A855F7"
                    icon={<UserCog size={28} />}
                />

            </DashboardGrid>

            <ChartsGrid>

                <ChartCard title="Colaboradores por Gestor">
                    <CollaboratorsChart />
                </ChartCard>

                <ChartCard title="Status Geral">
                    <StatusChart />
                </ChartCard>

            </ChartsGrid>

        </DashboardLayout>
    );
}