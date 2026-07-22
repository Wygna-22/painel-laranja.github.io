import "./Indicadores.css";
import {
    Users,
    Trophy,
    Target,
    TrendingUp,
} from "lucide-react";
import KpiCard from "../../components/KpiCard/KpiCard";
import SupervisorCard from "../../components/SupervisorCard/SupervisorCard";
import { useIndicadores } from "../../hooks/useIndicadores";
import IndicadorModal from "../../components/IndicadorModal/IndicadorModal";
import { useState } from "react";

export default function Indicadores() {
    const [openModal, setOpenModal] = useState(false);
    const {
        indicadores,
        loading,
        error,
        createIndicador,
    } = useIndicadores();

    if (loading) {
        return <h2>Carregando indicadores...</h2>;
    }

    if (error) {
        return <h2>{error}</h2>;
    }

    const coordenacao = indicadores.find(
            (i) => i.gestor === "Coordenação"
        );

    const gestores = indicadores.filter(
        (i) => i.gestor !== "Coordenação"
    );

    const totalPessoas = coordenacao?.qtd_pessoas ?? 0;

    const mediaPpc = coordenacao?.ppc ?? 0;

    const totalPontos = coordenacao?.pontos ?? 0;

    const totalMeta = coordenacao?.meta_mes ?? 0;

    return (

        <div className="indicadores-page">

            <div className="indicadores-header">
                <div>
                    <h1>Indicadores</h1>
                    <p>
                        Acompanhe o desempenho dos gestores e indicadores do mês.
                    </p>
                </div>

                <button 
                    className="novo-btn"
                    onClick={() => setOpenModal(true)}
                >
                    + Novo Indicador
                </button>
            </div>
            
            <div className="kpi-grid">

                <KpiCard
                    icon={Users}
                    title="Colaboradores"
                    value={totalPessoas}
                />

                <KpiCard
                    icon={TrendingUp}
                    title="PPC Médio"
                    value={mediaPpc.toFixed(2)}
                />

                <KpiCard
                    icon={Trophy}
                    title="Pontos"
                    value={totalPontos.toFixed(0)}
                />

                <KpiCard
                    icon={Target}
                    title="Meta"
                    value={totalMeta.toFixed(0)}
                />

            </div>

            {coordenacao && (
                <div className="coordenacao-container">
                    <SupervisorCard
                        nome={coordenacao.gestor}
                        pessoas={coordenacao.qtd_pessoas}
                        mes={`${coordenacao.mes}/${coordenacao.ano}`}
                        ppc={coordenacao.ppc}
                        pontos={coordenacao.pontos}
                        falta={coordenacao.falta_meta_mes}
                        esp={coordenacao.esperado_atual}
                        meta={coordenacao.meta_mes}
                        destaque
                    />
                </div>
            )}

            <div className="supervisores-grid">

                {gestores.map((indicador) => (

                    <SupervisorCard
                        key={indicador.id}
                        nome={indicador.gestor}
                        pessoas={indicador.qtd_pessoas}
                        mes={`${indicador.mes}/${indicador.ano}`}
                        ppc={indicador.ppc}
                        pontos={indicador.pontos}
                        falta={indicador.falta_meta_mes}
                        esp={indicador.esperado_atual}
                        meta={indicador.meta_mes}
                    />

                ))}

            </div>

            <IndicadorModal
                open={openModal}
                onClose={() => setOpenModal(false)}
                onSave={createIndicador}
            />
        </div>
    );
}