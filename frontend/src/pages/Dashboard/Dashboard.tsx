import DashboardLayout from "../../components/DashboardLayout/DashboardLayout";
import DashboardGrid from "../../components/DashboardGrid/DashboardGrid";
import ChartsGrid from "../../components/ChartsGrid/ChartsGrid";
import ChartCard from "../../components/ChartCard/ChartCard";

import CollaboratorsChart from "../../components/Charts/CollaboratorsChart";
import StatusChart from "../../components/Charts/StatusChart";
import KpiCard from "../../components/KpiCard/KpiCard";
import CityChart from "../../components/Charts/CityChart";
import SectorChart from "../../components/Charts/SectorChart";
import EventCard from "../../components/EventCard/EventCard";

import { useDashboard } from "../../hooks/useDashboard";
import VacationChart from "../../components/Charts/VacationChart";


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

            <div className="dashboard">

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

                    <ChartCard title="Distribuição por Cidade">
                        <CityChart
                            data={dashboard?.por_cidade ?? []}
                        />
                    </ChartCard>

                    <ChartCard title="Distribuição por Setor">
                        <SectorChart
                            data={dashboard?.por_setor ?? []}
                        />
                    </ChartCard>

                </ChartsGrid>

                <div className="dashboard-bottom">

                    <ChartCard title="Evolução das Férias">

                        <VacationChart
                            data={[
                                { mes: "Jan", quantidade: 2 },
                                { mes: "Fev", quantidade: 4 },
                                { mes: "Mar", quantidade: 5 },
                                { mes: "Abr", quantidade: 3 },
                                { mes: "Mai", quantidade: 6 },
                                { mes: "Jun", quantidade: 7 },
                            ]}
                        />

                    </ChartCard>

                    <EventCard>

                        {(dashboard?.ultimos_eventos ?? []).map((evento, index) => (

                            <div
                                key={index}
                                className="event-item"
                            >

                                <div
                                    style={{
                                        display: "flex",
                                        gap: 12,
                                        alignItems: "flex-start",
                                    }}
                                >

                                    <div
                                        style={{
                                            width: 10,
                                            height: 10,
                                            borderRadius: "50%",
                                            background: "#10B981",
                                            marginTop: 7,
                                            flexShrink: 0,
                                        }}
                                    />

                                    <div>

                                        <h4 className="event-title">
                                            {evento.titulo}
                                        </h4>

                                        <p className="event-user">
                                            {evento.colaborador}
                                        </p>

                                        <small className="event-date">
                                            {evento.data}
                                        </small>

                                    </div>

                                </div>

                            </div>

                        ))}

                    </EventCard>

                </div>

            </div>

        </DashboardLayout>
    );
}