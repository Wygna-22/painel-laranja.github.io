import "./SupervisorCard.css";
import { Pencil, Trash2 } from "lucide-react";

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
}: Props) {

    return (
        <div className="supervisor-card">
            <div className="supervisor-header">
                <div>
                    <h3>{nome}</h3>
                    <span>
                        {pessoas} colaboradores • {mes}
                    </span>
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
                    {ppc.toFixed(2)}
                </div>
                <small>Meta 8</small>
            </div>

            <div className="metric-grid">
                <div className="metric">
                    <small>Pontos</small>
                    <strong>{pontos.toLocaleString()}</strong>
                </div>

                <div className="metric">
                    <small>Falta</small>
                    <strong className="danger">
                        {falta.toLocaleString()}
                    </strong>
                </div>

                <div className="metric">
                    <small>ESP Atual</small>
                    <strong>{esp.toLocaleString()}</strong>
                </div>

                <div className="metric">
                    <small>Meta</small>
                    <strong>{meta.toLocaleString()}</strong>

                </div>
            </div>
        </div>
    );
}