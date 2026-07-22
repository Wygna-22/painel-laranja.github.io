import "./SupervisorCard.css";
import { Pencil, Trash2, UserRound } from "lucide-react";

interface Props {
    nome: string;
    pessoas: number;
    mes: string;

    ppc: number;

    pontos: number;
    falta: number;
    esp: number;
    meta: number;

    onEdit?: () => void;
    onDelete?: () => void;
    destaque?: boolean;
}

export default function SupervisorCard({
    nome,
    pessoas,
    mes,
    ppc,
    pontos,
    falta,
    esp,
    meta,
    onEdit,
    onDelete,
    destaque = false,
}: Props) {

    return (
       <div
            className={`supervisor-card ${
                destaque ? "coordenacao" : ""
            }`}
        >

            <div className="supervisor-header">

                <div className="supervisor-info">

                    <div className="avatar">
                        <UserRound size={32} strokeWidth={1.8}/>
                    </div>

                    <div>

                        <h3>{nome}</h3>

                        <span>
                            {pessoas} colaboradores • {mes}
                        </span>

                    </div>

                </div>

                <div className="supervisor-actions">

                    <button onClick={onEdit}>
                        <Pencil size={16}/>
                    </button>

                    <button onClick={onDelete}>
                        <Trash2 size={16}/>
                    </button>

                </div>

            </div>

            <div className="gauge-placeholder">

                <div className="gauge-circle">

                    <strong>
                        {ppc.toFixed(2)}
                    </strong>

                </div>

                <small>Meta 8</small>

            </div>

            <div className="progress">

                <div
                    className="progress-fill"
                    style={{
                        width: `${Math.min((ppc / 8) * 100, 100)}%`,
                    }}
                />

            </div>

            <div className="metric-grid">

                <div className="metric">

                    <small>Pontos</small>

                    <strong>
                        {pontos.toLocaleString()}
                    </strong>

                </div>

                <div className="metric">

                    <small>Falta/Mês</small>

                    <strong className="danger">
                        {falta.toLocaleString()}
                    </strong>

                </div>

                <div className="metric">

                    <small>ESP Atual</small>

                    <strong>
                        {esp.toLocaleString()}
                    </strong>

                </div>

                <div className="metric">

                    <small>Meta Mês</small>

                    <strong>
                        {meta.toLocaleString()}
                    </strong>

                </div>

            </div>

        </div>
    );
}