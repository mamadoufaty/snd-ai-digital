import Snd from '@/components/snd';

export default function Home() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 to-green-100">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-4xl font-bold text-center text-gray-800 mb-2">
            IA en production : des modèles qui fonctionnent, des résultats qui comptent
          </h1>
          <p className="text-center text-gray-600 mb-8">
            Une IA cloud pour planifier et gouverner le Sénégal
          </p>

          <div className="h-[700px]">
            <Snd />
          </div>

          <footer className="mt-8 text-center text-sm text-gray-500">
            <p>La nouvelle IA de Awa Faty : Poser les fondations du Sénégal numérique intelligent</p>
          </footer>
        </div>
      </div>
    </main>
  );
}
