import "./KpiCard.css";
import type { LucideIcon } from "lucide-react";

interface Props {
    icon: LucideIcon;
    title: string;
    value: string | number;
    subtitle?: string;
    color?: string;
}

export default function KpiCard({
    icon: Icon,
    title,
    value,
    subtitle,
    color = "#ff6b00",
}: Props) {

    return (
        <div className="kpi-card">
            <div
                className="kpi-icon"
                style={{ color }}
            >
                <Icon size={22} />
            </div>

            <div className="kpi-content">
                <h2>{value}</h2>
                <span>{title}</span>
                {subtitle && (
                    <small>{subtitle}</small>
                )}

            </div>
        </div>
    );
}